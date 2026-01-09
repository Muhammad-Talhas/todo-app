'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '../../lib/auth/context';
import apiClient from '../../lib/api/client';
import { Task } from '../../types/task';
import TaskList from '../../components/TaskList/TaskList';
import TaskForm from '../../components/TaskForm/TaskForm';
import AuthWrapper from '../../components/Auth/AuthWrapper';

const DashboardPage: React.FC = () => {
  const { state, logout } = useAuth();
  const [showForm, setShowForm] = useState(false);
  const [refreshTasks, setRefreshTasks] = useState(0);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // Fetch tasks to display stats
  useEffect(() => {
    if (state.user && state.token) {
      const fetchTasks = async () => {
        try {
          const response: any = await apiClient.getTasks(state.user!.id, state.token!);
          setTasks(response.tasks || response);
        } catch (err) {
          console.error('Failed to fetch tasks for stats:', err);
        }
      };
      fetchTasks();
    }
  }, [state.user, state.token, refreshTasks]);

  const handleTaskCreated = () => {
    setShowForm(false);
    setRefreshTasks(prev => prev + 1); // Trigger a refresh
  };

  const handleTaskUpdated = () => {
    setShowForm(false);
    setRefreshTasks(prev => prev + 1); // Trigger a refresh
  };

  if (!state.user) {
    return null; // AuthWrapper will handle the redirect
  }

  return (
    <AuthWrapper requireAuth>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
        {/* Mobile menu button */}
        <div className="sm:hidden fixed top-4 right-4 z-50">
          <button
            type="button"
            className="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            <span className="sr-only">Open menu</span>
            <svg
              className={`${mobileMenuOpen ? 'hidden' : 'block'} h-6 w-6`}
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <svg
              className={`${mobileMenuOpen ? 'block' : 'hidden'} h-6 w-6`}
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Mobile menu overlay */}
        {mobileMenuOpen && (
          <div className="sm:hidden fixed inset-0 z-40 bg-black bg-opacity-50" onClick={() => setMobileMenuOpen(false)}></div>
        )}

        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="bg-white rounded-2xl shadow-xl border border-gray-200 overflow-hidden">
            {/* Header Section */}
            <div className="bg-gradient-to-r from-indigo-600 to-purple-600 px-6 py-8 sm:px-8">
              <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between">
                <div>
                  <h1 className="text-3xl font-bold text-white">Your Tasks</h1>
                  <p className="mt-2 text-indigo-100">
                    {tasks.length > 0
                      ? `You have ${tasks.filter(t => !t.completed).length} pending tasks`
                      : 'Get started by creating your first task'
                    }
                  </p>
                </div>
                <div className="mt-4 sm:mt-0">
                  <button
                    onClick={() => setShowForm(!showForm)}
                    className="w-full sm:w-auto inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-lg shadow-sm text-indigo-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-200 transform hover:-translate-y-0.5"
                  >
                    {showForm ? (
                      <>
                        <svg className="-ml-1 mr-2 h-5 w-5 text-indigo-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                          <path fillRule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clipRule="evenodd" />
                        </svg>
                        Cancel
                      </>
                    ) : (
                      <>
                        <svg className="-ml-1 mr-2 h-5 w-5 text-indigo-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                          <path fillRule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clipRule="evenodd" />
                        </svg>
                        Add New Task
                      </>
                    )}
                  </button>
                </div>
              </div>
            </div>

            {/* Mobile menu panel */}
            {mobileMenuOpen && (
              <div className="sm:hidden bg-white border-b border-gray-200 px-6 py-4">
                <div className="flex flex-col space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-sm font-medium text-gray-900">Welcome, {state.user.email}</span>
                    <button
                      onClick={logout}
                      className="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded text-red-700 bg-red-100 hover:bg-red-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                    >
                      Sign out
                    </button>
                  </div>
                </div>
              </div>
            )}

            {/* Content Section */}
            <div className="px-6 py-8 sm:px-8 sm:py-10">
              {/* Task Form Section */}
              {showForm && state.user && (
                <div className="mb-10 animate-fadeIn">
                  <div className="flex items-center mb-6">
                    <h2 className="text-xl font-semibold text-gray-900">
                      {showForm ? 'Create New Task' : 'Edit Task'}
                    </h2>
                    <div className="ml-3 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800">
                      <svg className="-ml-0.5 mr-1 h-3 w-3 text-indigo-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                      </svg>
                      Form
                    </div>
                  </div>
                  <TaskForm
                    userId={state.user.id}
                    onTaskCreated={handleTaskCreated}
                    onTaskUpdated={handleTaskUpdated}
                    onCancel={() => setShowForm(false)}
                  />
                </div>
              )}

              {/* Task List Section */}
              <div className="animate-fadeIn">
                <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6 space-y-4 sm:space-y-0">
                  <h2 className="text-xl font-semibold text-gray-900">Task List</h2>
                  <div className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
                    {tasks.length} {tasks.length === 1 ? 'task' : 'tasks'}
                  </div>
                </div>
                {state.user && (
                  <TaskList userId={state.user.id} key={refreshTasks} />
                )}
              </div>
            </div>
          </div>

          {/* Desktop user menu */}
          <div className="hidden sm:flex justify-end mt-6">
            <div className="flex items-center space-x-4">
              <span className="text-sm text-gray-700">Welcome, {state.user.email}</span>
              <button
                onClick={logout}
                className="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded text-red-700 bg-red-100 hover:bg-red-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
              >
                Sign out
              </button>
            </div>
          </div>
        </div>
      </div>
    </AuthWrapper>
  );
};

export default DashboardPage;