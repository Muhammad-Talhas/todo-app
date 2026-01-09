// Simple authentication client for the Todo application
// Using a basic implementation compatible with Next.js 16

import { useState, useEffect } from 'react';

// Mock authentication functions for development
export const signIn = async (email: string, password: string) => {
  // In a real implementation, this would call your backend API
  const response = await fetch('/api/auth/signin', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (response.ok) {
    const data = await response.json();
    localStorage.setItem('authToken', data.token);
    return data;
  } else {
    throw new Error('Sign in failed');
  }
};

export const signUp = async (email: string, password: string, name?: string) => {
  // In a real implementation, this would call your backend API
  const response = await fetch('/api/auth/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password, name }),
  });

  if (response.ok) {
    const data = await response.json();
    localStorage.setItem('authToken', data.token);
    return data;
  } else {
    throw new Error('Sign up failed');
  }
};

export const signOut = () => {
  localStorage.removeItem('authToken');
};

export const useSession = () => {
  const [session, setSession] = useState<{ user: any; isLoading: boolean }>({
    user: null,
    isLoading: true
  });

  useEffect(() => {
    const token = localStorage.getItem('authToken');
    if (token) {
      // In a real implementation, you would validate the token with your backend
      // For now, we'll just decode a mock user from localStorage
      setSession({ user: { id: 1, email: 'user@example.com' }, isLoading: false });
    } else {
      setSession({ user: null, isLoading: false });
    }
  }, []);

  return session;
};