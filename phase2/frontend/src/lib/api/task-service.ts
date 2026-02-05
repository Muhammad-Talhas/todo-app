import { authClient } from "../auth/better-auth-client";

const BACKEND_URL = "http://127.0.0.1:8000";

export const taskService = {
    async getTasks() {
        const { data: session } = await authClient.getSession();
        const userId = session?.user?.id; // Get the ID from session

        if (!userId) throw new Error("No User ID found");

        // FIX: Added /api/ and the ${userId} to the URL
        const response = await fetch(`${BACKEND_URL}/api/${userId}/tasks`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                // Note: We bypassed Bearer token in backend, 
                // but keeping it won't hurt if the backend ignores it.
            }
        });

        if (!response.ok) throw new Error("Failed to fetch tasks");
        return response.json();
    },

    async createTask(taskData: any) {
        const { data: session } = await authClient.getSession();
        const userId = session?.user?.id;

        if (!userId) throw new Error("No User ID found");

        // FIX: Added /api/ and the ${userId} to the URL
        const response = await fetch(`${BACKEND_URL}/api/${userId}/tasks`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(taskData)
        });

        if (!response.ok) throw new Error("Failed to create task");
        return response.json();
    },

    async toggleTask(taskId: number) {
        const { data: session } = await authClient.getSession();
        const userId = session?.user?.id;

        // Note: URL includes both userId and taskId
        const response = await fetch(`${BACKEND_URL}/api/${userId}/tasks/${taskId}`, {
            method: "PATCH",
        });

        if (!response.ok) throw new Error("Failed to toggle task");
        return response.json();
    },

    async deleteTask(taskId: number) {
        const { data: session } = await authClient.getSession();
        const userId = session?.user?.id;

        const response = await fetch(`${BACKEND_URL}/api/${userId}/tasks/${taskId}`, {
            method: "DELETE",
        });

        if (!response.ok) throw new Error("Failed to delete task");
        return response.json();
    }
};