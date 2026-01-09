'use client';

import Link from 'next/link';
import { useState } from 'react';
import { motion } from 'framer-motion';

export default function HomePage() {
  const [tasks] = useState([
    'Complete project proposal',
    'Schedule team meeting',
    'Review quarterly reports',
  ]);

  const features = [
    {
      title: 'Task Management',
      description:
        'Create, organize, and track your tasks with ease. Add titles, descriptions, and due dates to stay on top of your work.',
      icon: (
        <svg
          className="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
          />
        </svg>
      ),
    },
    {
      title: 'Secure Authentication',
      description:
        'Your data is protected with secure authentication. Each user has their own private task space.',
      icon: (
        <svg
          className="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M12 11c0-1.105.895-2 2-2s2 .895 2 2v4h-4v-4zM12 11V7a4 4 0 018 0v4"
          />
        </svg>
      ),
    },
    {
      title: 'Due Dates & Reminders',
      description:
        'Set due dates for your tasks and get visual indicators for overdue items to never miss a deadline.',
      icon: (
        <svg
          className="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
      ),
    },
    {
      title: 'Progress Tracking',
      description:
        'Mark tasks as complete to track your progress and visualize your accomplishments.',
      icon: (
        <svg
          className="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 12l2 2 4-4"
          />
        </svg>
      ),
    },
  ];

  const fadeInUp = {
    hidden: { opacity: 0, y: 20 },
    visible: (i = 1) => ({
      opacity: 1,
      y: 0,
      transition: { delay: i * 0.2, duration: 0.6 },
    }),
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 flex flex-col">
      {/* Navigation */}
      <motion.nav
        className="bg-white shadow-sm sticky top-0 z-50"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center space-x-2">
              <svg
                className="h-8 w-8 text-blue-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2"
                />
              </svg>
              <span className="text-xl font-bold text-gray-900">TodoApp</span>
            </div>
            <div className="flex items-center space-x-4">
              <Link
                href="/login"
                className="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900"
              >
                Login
              </Link>
              <Link
                href="/signup"
                className="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-md"
              >
                Sign Up
              </Link>
            </div>
          </div>
        </div>
      </motion.nav>

      {/* Hero Section */}
      <section className="relative flex flex-col lg:flex-row items-center max-w-7xl mx-auto px-4 py-16 gap-8 lg:gap-16">
        <motion.div
          className="lg:w-1/2 text-center lg:text-left"
          initial="hidden"
          animate="visible"
          variants={fadeInUp}
        >
          <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-gray-900">
            Get things done{' '}
            <span className="text-blue-600">with TodoApp</span>
          </h1>
          <p className="mt-4 sm:mt-6 text-gray-500 sm:text-lg md:text-xl max-w-lg">
            A beautiful, intuitive task management app that helps you stay
            organized and productive. Keep track of everything, from daily
            tasks to long-term goals.
          </p>
          <div className="mt-6 sm:mt-8 flex flex-col sm:flex-row sm:justify-center lg:justify-start gap-3">
            <motion.div whileHover={{ scale: 1.05 }}>
              <Link
                href="/signup"
                className="px-8 py-3 md:px-10 md:py-4 text-lg font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 transition"
              >
                Get Started
              </Link>
            </motion.div>
            <motion.div whileHover={{ scale: 1.05 }}>
              <Link
                href="/login"
                className="px-8 py-3 md:px-10 md:py-4 text-lg font-medium text-blue-700 bg-blue-100 rounded-md hover:bg-blue-200 transition"
              >
                Sign in
              </Link>
            </motion.div>
          </div>
        </motion.div>

        {/* Tasks Preview */}
        <motion.div
          className="lg:w-1/2 flex justify-center lg:justify-end"
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.6 }}
        >
          <div className="bg-gradient-to-r from-blue-100 to-indigo-200 rounded-xl p-6 w-full max-w-md shadow-lg">
            <div className="bg-white rounded-xl p-6 shadow">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-medium text-gray-900">Your Tasks</h3>
                <span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                  {tasks.length} tasks
                </span>
              </div>
              <ul className="space-y-3">
                {tasks.map((task, index) => (
                  <motion.li
                    key={index}
                    className="flex items-center gap-3"
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.1 }}
                  >
                    <input
                      type="checkbox"
                      className="h-4 w-4 text-blue-600 rounded"
                    />
                    <span className="text-gray-700 text-sm">{task}</span>
                  </motion.li>
                ))}
              </ul>
              <div className="mt-4 flex gap-2">
                <input
                  type="text"
                  placeholder="Add a new task..."
                  className="flex-1 px-3 py-2 rounded-l-md border border-gray-300 focus:ring-blue-500 focus:border-blue-500 outline-none text-sm"
                />
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  className="px-4 py-2 text-white bg-blue-600 rounded-r-md hover:bg-blue-700 transition text-sm"
                >
                  Add
                </motion.button>
              </div>
            </div>
          </div>
        </motion.div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          {/* Feature Heading */}
          <motion.div
            className="text-center mb-12"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-semibold text-blue-600 tracking-wide uppercase">
              Features
            </h2>
            <p className="mt-2 text-3xl sm:text-4xl md:text-5xl font-extrabold text-gray-900">
              Everything you need to manage tasks
            </p>
            <p className="mt-4 max-w-2xl mx-auto text-lg sm:text-xl md:text-2xl text-gray-500">
              Our powerful features help you stay organized and productive.
            </p>
          </motion.div>

          {/* Feature Cards */}
          <div className="grid gap-10 md:grid-cols-2 lg:grid-cols-2">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                className="relative pl-20 pr-4 py-6 bg-white rounded-xl shadow hover:shadow-lg transition cursor-pointer"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.2 }}
                whileHover={{ scale: 1.03 }}
              >
                <div className="absolute top-1/2 -translate-y-1/2 left-6 flex items-center justify-center h-12 w-12 rounded-md bg-blue-500 text-white">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-gray-900">{feature.title}</h3>
                <p className="mt-2 text-gray-500 text-base sm:text-lg">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-blue-700">
        <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8 lg:flex lg:items-center lg:justify-between">
          <motion.h2
            className="text-3xl font-extrabold text-white sm:text-4xl"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <span className="block">Ready to get started?</span>
            <span className="block text-blue-200">
              Start managing your tasks today.
            </span>
          </motion.h2>
          <div className="mt-8 flex lg:mt-0 lg:flex-shrink-0 gap-3">
            <motion.div whileHover={{ scale: 1.05 }}>
              <Link
                href="/signup"
                className="px-5 py-3 text-base font-medium rounded-md text-blue-600 bg-white hover:bg-blue-50 transition"
              >
                Get started
              </Link>
            </motion.div>
            <motion.div whileHover={{ scale: 1.05 }}>
              <Link
                href="/login"
                className="px-5 py-3 text-base font-medium rounded-md text-white bg-blue-800 hover:bg-blue-900 transition"
              >
                Sign in
              </Link>
            </motion.div>
          </div>
        </div>
      </section>
    </div>
  );
}
