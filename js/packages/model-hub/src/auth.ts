/**
 * Authentication
 */

export async function authenticate(token: string): Promise<boolean> { return token.length > 0; }
export function getToken(): string | null { return process.env.NF_TOKEN || null; }

