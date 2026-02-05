'use client';

import React, { useState } from 'react';
import { Task } from '../../types/task';
import apiClient from '../../lib/api/client';

interface TaskFormProps {
  userId: string; // CHANGED: now a string to match Better Auth
  token: string;  // ADDED: required to authorize the API call
  onTaskCreated?: () => void;
  onTaskUpdated?: () => void;
  task?: Pick<Task, 'id' | 'title' | 'description' | 'due_date'>;
  onCancel?: () => void;
}

interface TaskData {
  title: string;
  description?: string;
  due_date?: string;
}

const TaskForm: React.FC<TaskFormProps> = ({ 
  userId, 
  token, 
  onTaskCreated, 
  onTaskUpdated, 
  task, 
  onCancel 
}) => {
  const [formData, setFormData] = useState<TaskData>({
    title: task?.title || '',
    description: task?.description || '',
    due_date: task?.due_date || '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // ... logic ...

    // Create a copy of the data
    const payload: any = { ...formData };

    // If due_date is empty, falsy, or an empty string, remove it or set to null
    if (!payload.due_date || payload.due_date === "") {
        payload.due_date = null; 
    }

    try {
        // Send the PAYLOAD, not the formData
        await apiClient.createTask(userId, payload);
        
      // Reset form on success
      setFormData({
        title: '',
        description: '',
        due_date: '',
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to save task');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden transition-all duration-300 hover:shadow-xl">
      <div className="p-6 sm:p-8">
        <form onSubmit={handleSubmit} className="space-y-6">
          {error && (
            <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded-lg animate-fadeIn">
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
          )}

          <div className="space-y-4">
            <div>
              <label htmlFor="title" className="block text-sm font-semibold text-gray-800 mb-2">
                Task Title *
              </label>
              <input
                type="text"
                name="title"
                id="title"
                required
                value={formData.title}
                onChange={handleChange}
                className="block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 transition-all"
                placeholder="Enter task title..."
              />
            </div>

            <div>
              <label htmlFor="description" className="block text-sm font-semibold text-gray-800 mb-2">
                Description
              </label>
              <textarea
                id="description"
                name="description"
                rows={4}
                value={formData.description}
                onChange={handleChange}
                className="block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 transition-all resize-none"
                placeholder="Describe your task..."
              />
            </div>

            <div>
              <label htmlFor="due_date" className="block text-sm font-semibold text-gray-800 mb-2">
                Due Date
              </label>
              <input
                type="date"
                name="due_date"
                id="due_date"
                value={formData.due_date}
                onChange={handleChange}
                className="block w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 transition-all"
              />
            </div>
          </div>

          <div className="pt-4 flex flex-col sm:flex-row sm:space-x-4 space-y-4 sm:space-y-0">
            {onCancel && (
              <button
                type="button"
                onClick={onCancel}
                className="w-full sm:w-auto px-6 py-3 font-medium text-gray-700 bg-gray-100 rounded-lg border border-gray-300 hover:bg-gray-200"
              >
                Cancel
              </button>
            )}
            <button
              type="submit"
              disabled={loading}
              className="w-full sm:w-auto px-6 py-3 font-medium text-white bg-gradient-to-r from-indigo-600 to-purple-600 rounded-lg hover:shadow-lg disabled:opacity-70 transition-all"
            >
              {loading ? (task ? 'Updating...' : 'Creating...') : (task ? 'Update Task' : 'Create Task')}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default TaskForm;