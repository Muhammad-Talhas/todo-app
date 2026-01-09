// TypeScript types for the Todo application

export interface User {
  id: number;
  email: string;
  name?: string;
  created_at: string;
  updated_at: string;
  is_active: boolean;
}

export interface UserLoginRequest {
  email: string;
  password: string;
}

export interface UserLoginResponse {
  access_token: string;
  token_type: string;
  user: {
    id: number;
    email: string;
    name?: string;
  };
}

export interface UserRegistrationRequest {
  email: string;
  password: string;
  name?: string;
}

export interface UserRegistrationResponse extends UserLoginResponse {}

export interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  user_id: number;
  created_at: string;
  updated_at: string;
  due_date?: string;
}

export interface TaskCreateRequest {
  title: string;
  description?: string;
  due_date?: string;
}

export interface TaskUpdateRequest {
  title?: string;
  description?: string;
  due_date?: string;
}

export interface TaskPatchRequest {
  completed: boolean;
}

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  message?: string;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}