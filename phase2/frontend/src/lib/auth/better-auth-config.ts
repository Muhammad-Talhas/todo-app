// Better Auth configuration for the Todo application

import { betterAuth } from "better-auth";

export const auth = betterAuth({
  secret: process.env.BETTER_AUTH_SECRET || "fallback-secret-key-for-development",
  database: {
    provider: "sqlite", // or "postgresql", "mysql", etc.
    url: process.env.DATABASE_URL || "./db.sqlite",
  },
  socialProviders: {
    // Add social providers if needed
  },
  emailAndPassword: {
    enabled: true,
    requireEmailVerification: false, // Set to true in production
  },
  account: {
    // Account configuration options if needed
  },
  session: {
    expiresIn: 7 * 24 * 60 * 60, // 7 days
    updateAge: 24 * 60 * 60, // 24 hours
  },
});