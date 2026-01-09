'use client';

import React, { useEffect } from 'react';
import { useAuth } from '../../lib/auth/context';
import { useRouter } from 'next/navigation';

interface AuthWrapperProps {
  children: React.ReactNode;
  requireAuth?: boolean; // If true, redirects to login if not authenticated
  redirectIfAuth?: boolean; // If true, redirects to dashboard if authenticated
}

const AuthWrapper: React.FC<AuthWrapperProps> = ({
  children,
  requireAuth = false,
  redirectIfAuth = false
}) => {
  const { state } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (requireAuth && !state.isAuthenticated && !state.isLoading) {
      router.push('/login');
    } else if (redirectIfAuth && state.isAuthenticated && !state.isLoading) {
      router.push('/dashboard');
    }
  }, [state.isAuthenticated, state.isLoading, requireAuth, redirectIfAuth, router]);

  // Show loading state while checking authentication
  if (state.isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  // Don't render children if redirect is needed
  if (
    (requireAuth && !state.isAuthenticated) ||
    (redirectIfAuth && state.isAuthenticated)
  ) {
    return null;
  }

  return <>{children}</>;
};

export default AuthWrapper;