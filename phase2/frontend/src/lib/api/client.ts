// API Client Service for Todo Application

interface ApiConfig {
  baseUrl: string;
  headers?: Record<string, string>;
}

class ApiClient {
  private config: ApiConfig;

  constructor(config: ApiConfig) {
    this.config = config;
  }

  // Helper method to get auth headers
  private getAuthHeaders(token?: string): Record<string, string> {
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    return headers;
  }

  // Generic request method
  private async request<T>(
    endpoint: string,
    options: RequestInit = {},
    token?: string
  ): Promise<T> {
    const url = `${this.config.baseUrl}${endpoint}`;

    const config: RequestInit = {
      headers: {
        ...this.getAuthHeaders(token),
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);

      if (!response.ok) {
        const errorData = await response.text();
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorData}`);
      }

      return await response.json();
    } catch (error) {
      console.error(`API request failed: ${endpoint}`, error);
      throw error;
    }
  }

  // Authentication methods
  login = (email: string, password: string) => {
    return this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  };

  signup = (email: string, password: string, name?: string) => {
    return this.request('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ email, password, name }),
    });
  };

  // Task methods
  getTasks = (userId: number, token: string) => {
    return this.request(`/api/${userId}/tasks`, {
      method: 'GET',
    }, token);
  };

  createTask = (userId: number, taskData: any, token: string) => {
    return this.request(`/api/${userId}/tasks`, {
      method: 'POST',
      body: JSON.stringify(taskData),
    }, token);
  };

  getTask = (userId: number, taskId: number, token: string) => {
    return this.request(`/api/${userId}/tasks/${taskId}`, {
      method: 'GET',
    }, token);
  };

  updateTask = (userId: number, taskId: number, taskData: any, token: string) => {
    return this.request(`/api/${userId}/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    }, token);
  };

  deleteTask = (userId: number, taskId: number, token: string) => {
    return this.request(`/api/${userId}/tasks/${taskId}`, {
      method: 'DELETE',
    }, token);
  };

  updateTaskCompletion = (userId: number, taskId: number, completed: boolean, token: string) => {
    return this.request(`/api/${userId}/tasks/${taskId}/complete`, {
      method: 'PATCH',
      body: JSON.stringify({ completed }),
    }, token);
  };
}

// Create API client instance with base URL from environment
const apiClient = new ApiClient({
  baseUrl: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
});

export default apiClient;
export { ApiClient };