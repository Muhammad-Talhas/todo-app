'use client';

import React, { useEffect } from 'react';
import { useAuth } from '../../lib/auth/context';
import { useRouter } from 'next/navigation';

interface AuthWrapperProps {
  children: React.ReactNode;
  requireAuth?: boolean;   // If true, redirects to login if not authenticated
  redirectIfAuth?: boolean; // If true, redirects to dashboard if authenticated
}

const AuthWrapper: React.FC<AuthWrapperProps> = ({
  children,
  requireAuth = false,
  redirectIfAuth = false
}) => {
  const { state } = useAuth();
  const router = useRouter();

  // We determine authentication based on the presence of a user object
  const isUserAuthenticated = !!state.user;

  useEffect(() => {
    // 1. Safety Check: Only act once loading is completely finished
    if (state.isLoading) return;

    if (requireAuth && !isUserAuthenticated) {
      // User is NOT logged in but trying to access a protected page (Dashboard)
      router.push('/login');
    } else if (redirectIfAuth && isUserAuthenticated) {
      // User IS logged in but trying to access an auth page (Login/Register)
      router.push('/dashboard');
    }
  }, [isUserAuthenticated, state.isLoading, requireAuth, redirectIfAuth, router]);

  // 2. Show loading state while Better Auth checks for a session cookie
  if (state.isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <div className="flex flex-col items-center gap-4">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-600"></div>
          <p className="text-gray-500 font-medium animate-pulse">Syncing Session...</p>
        </div>
      </div>
    );
  }

  // 3. Prevent rendering children if a redirect is imminent
  // This stops the "flicker" where the dashboard shows for 1ms before pushing to login
  if (requireAuth && !isUserAuthenticated) return null;
  if (redirectIfAuth && isUserAuthenticated) return null;

  return <>{children}</>;
};

export default AuthWrapper;