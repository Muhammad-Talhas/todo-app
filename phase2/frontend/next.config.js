/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbo: false, // ⛔ disable Turbopack
  },

  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
    NEXT_PUBLIC_BETTER_AUTH_URL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL,
  },
};

module.exports = nextConfig;
