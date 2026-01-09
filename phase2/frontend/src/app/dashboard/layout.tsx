'use client';

import React from 'react';
import Link from 'next/link';
import { useAuth } from '../../lib/auth/context';
import AuthWrapper from '../../components/Auth/AuthWrapper';

const DashboardLayout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { logout, state } = useAuth();

  const handleLogout = () => {
    logout();
  };

  return (
    <AuthWrapper requireAuth>
      <div className="min-h-screen bg-gray-50">
        {/* Navigation */}
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <h1 className="text-xl font-semibold text-gray-900">Todo App</h1>
                </div>
                <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                  <Link
                    href="/dashboard"
                    className="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                  >
                    Dashboard
                  </Link>
                </div>
              </div>
              <div className="flex items-center">
                <div className="ml-3 relative">
                  <div className="flex items-center space-x-4">
                    {state.user && (
                      <span className="text-gray-700 text-sm font-medium">
                        Welcome, {state.user.name || state.user.email.split('@')[0]}
                      </span>
                    )}
                    <button
                      onClick={handleLogout}
                      className="bg-gray-800 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                    >
                      <span className="sr-only">Logout</span>
                      <span className="inline-block h-8 w-8 rounded-full bg-indigo-600 flex items-center justify-center text-white text-xs font-bold">
                        {state.user?.name?.charAt(0).toUpperCase() || state.user?.email.charAt(0).toUpperCase() || 'U'}
                      </span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </nav>

        <main>
          {children}
        </main>
      </div>
    </AuthWrapper>
  );
};

export default DashboardLayout;