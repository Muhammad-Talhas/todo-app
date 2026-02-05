import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins"; // 1. Import the JWT plugin

export const auth = betterAuth({
    secret: process.env.BETTER_AUTH_SECRET || "fallback-secret-key",
    baseURL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || "http://localhost:3000",
    
    // 2. Add the JWT Plugin here
    plugins: [
        jwt({
            jwt: {
                expirationTime: "1d", // Tokens last 1 day
            }
        })
    ],

    socialProviders: {
        google: {
            clientId: process.env.GOOGLE_CLIENT_ID!,
            clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
        },
    },
    emailAndPassword: {
        enabled: true,
    },
    session: {
        expiresIn: 7 * 24 * 60 * 60, // 7 days
    },
    cookies: {
        domain: undefined, 
        path: "/",
        secure: process.env.NODE_ENV === "production",
        httpOnly: true,
        sameSite: "lax", 
    }
});