'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/lib/auth/context';

const LoginPage: React.FC = () => {
  const router = useRouter();
  const { login, oauthLogin, state } = useAuth();

  // Local state for form fields
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [localLoading, setLocalLoading] = useState(false);

  // Validation states
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const validateForm = () => {
    let isValid = true;
    setEmailError('');
    setPasswordError('');

    if (!email) {
      setEmailError('Email is required');
      isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      setEmailError('Email address is invalid');
      isValid = false;
    }

    if (!password) {
      setPasswordError('Password is required');
      isValid = false;
    }

    return isValid;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!validateForm()) return;

    setLocalLoading(true);
    setError(null);

    try {
      await login(email, password);
      // Successful login updates the AuthContext state
      router.push('/dashboard');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Invalid credentials');
      setLocalLoading(false);
    }
  };

  const handleSocialLogin = async (provider: 'google' | 'github') => {
    setError(null);
    try {
      await oauthLogin(provider);
      // Note: Better Auth handles the redirect automatically for social logins
    } catch (err) {
      setError('Social login failed. Please try again.');
    }
  };

  // Determine if we should show a loading state
  const isProcessing = localLoading || state.isLoading;

  return (
    <div className="bg-gray-50 min-h-screen flex items-center justify-center px-4">
      <div className="max-w-[480px] w-full">
        <div className="p-6 sm:p-8 rounded-2xl bg-white border border-gray-200 shadow-sm">
          <h1 className="text-slate-900 text-center text-3xl font-semibold mb-8">Sign in</h1>

          {/* Social Login Buttons */}
          <div className="space-y-4">
            <button
              type="button"
              onClick={() => handleSocialLogin('github')}
              className="px-4 py-2.5 flex items-center justify-center rounded-md text-white text-sm font-medium bg-gray-800 hover:bg-gray-900 w-full transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20px" fill="white" className="mr-3" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
              </svg>
              Continue with GitHub
            </button>
            
            <button
              type="button"
              onClick={() => handleSocialLogin('google')}
              className="px-4 py-2.5 flex items-center justify-center rounded-md text-slate-700 text-sm font-medium border border-gray-300 bg-white hover:bg-gray-50 w-full transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20px" className="mr-3" viewBox="0 0 48 48">
                <path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z" />
                <path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z" />
                <path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z" />
                <path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z" />
              </svg>
              Continue with Google
            </button>
          </div>

          <div className="relative my-8">
            <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-gray-200"></div></div>
            <div className="relative flex justify-center text-sm">
              <span className="px-2 bg-white text-gray-400">or use email</span>
            </div>
          </div>

          <form onSubmit={handleSubmit} className="space-y-5">
            {error && (
              <div className="p-3 text-sm text-red-600 bg-red-50 border border-red-200 rounded-lg text-center">
                {error}
              </div>
            )}

            <div>
              <label className="text-slate-700 text-sm font-medium mb-1.5 block">Email Address</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className={`w-full px-4 py-2.5 text-sm border rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition-all ${emailError ? 'border-red-500' : 'border-gray-300'}`}
                placeholder="name@company.com"
              />
              {emailError && <p className="mt-1 text-xs text-red-500">{emailError}</p>}
            </div>

            <div>
              <label className="text-slate-700 text-sm font-medium mb-1.5 block">Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className={`w-full px-4 py-2.5 text-sm border rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition-all ${passwordError ? 'border-red-500' : 'border-gray-300'}`}
                placeholder="••••••••"
              />
              {passwordError && <p className="mt-1 text-xs text-red-500">{passwordError}</p>}
            </div>

            <button
              type="submit"
              disabled={isProcessing}
              className="w-full py-3 px-4 text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg font-medium transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
            >
              {isProcessing ? 'Please wait...' : 'Sign in'}
            </button>
          </form>

          <p className="text-center mt-8 text-sm text-gray-500">
            Don't have an account?{' '}
            <Link href="/signup" className="text-indigo-600 font-semibold hover:underline">
              Sign up
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;