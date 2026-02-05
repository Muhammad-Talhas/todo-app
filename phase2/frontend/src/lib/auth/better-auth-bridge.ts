// frontend/src/lib/auth/better-auth-bridge.ts
'use client';

/**
 * Handles OAuth login with Better Auth API routes
 */

interface OAuthResult {
  backendToken: string;
  user: {
    id: string;
    email: string;
    name?: string;
  };
}

export async function signInWithProvider(provider: 'github' | 'google'): Promise<OAuthResult> {
  return new Promise<OAuthResult>((resolve, reject) => {
    // Create a hidden iframe to handle the OAuth flow
    const iframe = document.createElement('iframe');
    iframe.style.display = 'none';
    document.body.appendChild(iframe);

    // Listen for messages from the iframe
    const handleMessage = (event: MessageEvent) => {
      if (event.origin !== window.location.origin) return;

      const { data } = event;
      if (data?.type === 'oauth-success' && data?.token && data?.user) {
        window.removeEventListener('message', handleMessage);
        document.body.removeChild(iframe);

        // Sync with backend
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/oauth-sync`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            provider,
            email: data.user.email,
            name: data.user.name || data.user.email.split('@')[0],
          }),
        })
        .then(response => response.json())
        .then(backendData => {
          resolve({
            backendToken: backendData.access_token,
            user: backendData.user
          });
        })
        .catch(() => {
          // If backend sync fails, return the Better Auth data
          resolve({
            backendToken: data.token,
            user: data.user
          });
        });
      } else if (data?.type === 'oauth-error') {
        window.removeEventListener('message', handleMessage);
        document.body.removeChild(iframe);
        reject(new Error(data.message || 'OAuth login failed'));
      }
    };

    window.addEventListener('message', handleMessage);

    // Navigate the iframe to the OAuth provider
    iframe.src = `/api/auth/${provider.toLowerCase()}`;
  });
}
