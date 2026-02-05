'use client';

import React, { createContext, useContext, useEffect, useState } from 'react';
import { authClient } from './better-auth-client';

interface AuthState {
  user: any | null;
  token: string | null;
  isLoading: boolean;
  error: string | null;
}

interface AuthContextType {
  state: AuthState;
  login: (email: string, password: string) => Promise<void>;
  oauthLogin: (provider: 'google' | 'github') => Promise<void>;
  logout: () => Promise<void>;
  refreshSession: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [state, setState] = useState<AuthState>({
    user: null,
    token: null,
    isLoading: true,
    error: null,
  });

  const refreshSession = async () => {
    try {
      const { data, error } = await authClient.getSession();
      if (error || !data) {
        setState(prev => ({ ...prev, isLoading: false, user: null, token: null }));
        return;
      }

      setState({
        user: data.user,
        // Better Auth standard structure: data.session.token
        token: data.session?.token || (data as any).token || null,
        isLoading: false,
        error: null,
      });
    } catch (err) {
      setState(prev => ({ ...prev, isLoading: false }));
    }
  };

  useEffect(() => {
    refreshSession();
  }, []);

  // Renamed internally to 'signInWithEmail' to avoid ts(2451) conflict
  const signInWithEmail = async (email: string, password: string) => {
    const result = await authClient.signIn.email({
      email,
      password,
    });

    if (result.error) throw new Error(result.error.message);

    if (result.data) {
      setState({
        user: result.data.user,
        token: (result.data as any).token || (result.data as any).session?.token || null,
        isLoading: false,
        error: null,
      });
    }
  };

  const oauthLogin = async (provider: 'google' | 'github') => {
    try {
      await authClient.signIn.social({
        provider,
        callbackURL: '/dashboard',
      });
    } catch (err) {
      console.error("OAuth Error:", err);
    }
  };

  const logout = async () => {
    await authClient.signOut();
    setState({ user: null, token: null, isLoading: false, error: null });
    window.location.href = '/login';
  };

  return (
    <AuthContext.Provider 
      value={{ 
        state, 
        login: signInWithEmail, // Mapping the internal function to the 'login' key
        oauthLogin, 
        logout, 
        refreshSession 
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};