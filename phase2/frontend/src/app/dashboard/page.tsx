'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '../../lib/auth/context';
import TaskList from '../../components/TaskList/TaskList';
import TaskForm from '../../components/TaskForm/TaskForm';
import { useRouter } from 'next/navigation';

const DashboardPage = () => {
  const { state, logout } = useAuth();
  const router = useRouter();
  const [showForm, setShowForm] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);

  // Use effect to handle the redirect safely
  useEffect(() => {
    if (!state.isLoading && !state.user) {
      router.push('/login');
    }
  }, [state.user, state.isLoading, router]);

  // 1. Loading State: Wait for the session check to finish
  if (state.isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto"></div>
          <p className="mt-4 text-gray-600 font-medium">Authenticating session...</p>
        </div>
      </div>
    );
  }

  // 2. Prevent UI flash if user is null (useEffect will handle redirect)
  if (!state.user) return null;

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white border-b border-gray-200 p-4 sticky top-0 z-10">
        <div className="max-w-5xl mx-auto flex justify-between items-center">
          <span className="font-bold text-indigo-600 text-xl">TaskMaster</span>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-500">{state.user.email}</span>
            <button onClick={logout} className="text-sm font-medium text-red-600">Logout</button>
          </div>
        </div>
      </nav>

      <main className="max-w-5xl mx-auto p-6">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-2xl font-bold text-gray-900">My Tasks</h1>
          <button 
            onClick={() => setShowForm(!showForm)}
            className="bg-indigo-600 text-white px-5 py-2.5 rounded-lg font-medium"
          >
            {showForm ? 'Cancel' : '+ New Task'}
          </button>
        </div>

        {showForm && (
          <div className="mb-8">
            <TaskForm 
              userId={state.user.id} 
              token={state.token || ''} 
              onTaskCreated={() => {
                setShowForm(false);
                setRefreshKey(k => k + 1);
              }}
            />
          </div>
        )}

        <TaskList 
          userId={state.user.id} 
          token={state.token || ''} 
          key={refreshKey}
        />
      </main>
    </div>
  );
};

export default DashboardPage;