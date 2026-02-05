'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '../../lib/auth/context';
import { Task } from '../../types/task';
import apiClient from '../../lib/api/client';

interface TaskListProps {
  userId: string; // CHANGED: now a string to match Better Auth IDs
  token: string;  // ADDED: passed from the Dashboard for API calls
}

const TaskList: React.FC<TaskListProps> = ({ userId, token }) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Use the props for fetching to ensure reliability
  useEffect(() => {
    fetchTasks();
  }, [userId, token]);

  const fetchTasks = async () => {
    if (!token) return;

    try {
      setLoading(true);
      // Using the string userId and the provided token
      const response: any = await apiClient.getTasks(userId, token);
      setTasks(response.tasks || response); // Handle different response formats
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch tasks');
    } finally {
      setLoading(false);
    }
  };

  const toggleTaskCompletion = async (taskId: number, completed: boolean) => {
    if (!token) return;

    try {
      // Toggle the completion status on the backend
      await apiClient.updateTaskCompletion(userId, taskId, !completed, token);
      
      // Update the task in the local state immediately for a snappy UI
      setTasks(prevTasks =>
        prevTasks.map(task =>
          task.id === taskId ? { ...task, completed: !completed } : task
        )
      );
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update task');
    }
  };

  const deleteTask = async (taskId: number) => {
    if (!token) return;

    try {
      await apiClient.deleteTask(userId, taskId, token);
      // Remove the task from local state
      setTasks(prevTasks => prevTasks.filter(task => task.id !== taskId));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete task');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center py-12">
        <div className="relative">
          <div className="w-12 h-12 border-4 border-indigo-200 rounded-full animate-spin border-t-indigo-600"></div>
          <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-indigo-600">
            <svg className="w-6 h-6 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
            </svg>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded-lg mb-6">
        <div className="flex">
          <div className="flex-shrink-0">
            <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
            </svg>
          </div>
          <div className="ml-3">
            <p className="text-sm text-red-700">{error}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden transition-all duration-300">
      <div className="divide-y divide-gray-200">
        {tasks.length === 0 ? (
          <div className="py-16 px-6 text-center">
            <div className="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-gray-100">
              <svg className="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h3 className="mt-4 text-lg font-medium text-gray-900">No tasks</h3>
            <p className="mt-1 text-sm text-gray-500">Get started by creating a new task.</p>
          </div>
        ) : (
          tasks.map((task) => (
            <div
              key={task.id}
              className={`p-6 transition-all duration-200 hover:bg-gray-50 ${task.completed ? 'bg-green-50/30' : ''}`}
            >
              <div className="flex items-start space-x-4">
                <div className="flex items-center h-5 pt-0.5">
                  <input
                    type="checkbox"
                    checked={task.completed}
                    onChange={() => toggleTaskCompletion(task.id, task.completed)}
                    className="h-5 w-5 rounded border-gray-300 text-indigo-600 cursor-pointer"
                  />
                </div>

                <div className="min-w-0 flex-1">
                  <div className="flex items-center justify-between">
                    <p className={`text-base font-semibold ${task.completed ? 'text-gray-500 line-through' : 'text-gray-900'}`}>
                      {task.title}
                    </p>

                    <button
                      onClick={() => deleteTask(task.id)}
                      className="inline-flex items-center px-3 py-1.5 text-xs font-medium rounded-full text-red-700 bg-red-100 hover:bg-red-200 transition-colors"
                    >
                      Delete
                    </button>
                  </div>

                  {task.description && (
                    <p className={`mt-2 text-sm ${task.completed ? 'text-gray-400' : 'text-gray-500'}`}>
                      {task.description}
                    </p>
                  )}

                  {task.due_date && (
                    <div className="mt-3 flex items-center text-xs text-gray-500">
                      <svg className="mr-1.5 h-4 w-4" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clipRule="evenodd" />
                      </svg>
                      Due: {new Date(task.due_date).toLocaleDateString()}
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default TaskList;