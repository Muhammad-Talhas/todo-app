import { createAuthClient } from "better-auth/client";

export const authClient = createAuthClient({
    baseURL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || 'http://localhost:3000',
    fetchOptions: {
        credentials: "include",  // Important for sending cookies with requests
    },
    // Enable session caching for better performance
    session: {
        cookieCache: {
            enabled: true,
            maxAge: 60 * 60 * 24 // 1 day
        }
    }
});