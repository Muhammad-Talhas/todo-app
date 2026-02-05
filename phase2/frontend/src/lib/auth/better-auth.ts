import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";
import { Pool } from "pg";

export const auth = betterAuth({
  secret: process.env.BETTER_AUTH_SECRET,
  // Use a fallback to localhost to ensure cookies work in dev
  baseURL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || "http://localhost:3000",
  
  database: new Pool({
    connectionString: process.env.DATABASE_URL,
    ssl: { rejectUnauthorized: false }, // Common fix for Supabase/Neon SSL errors
  }),

  account: {
    accountLinking: {
      enabled: true,
    }
  },

  plugins: [
    jwt({
      jwt: { expirationTime: "7d" }
    })
  ],

  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    },
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    },
  },

  emailAndPassword: {
    enabled: true,
  },
  
  // ADD THIS: Ensures cookies are handled correctly on localhost
  advanced: {
    useSecureCookies: false, // Forces cookies to work on http://localhost
  }
});