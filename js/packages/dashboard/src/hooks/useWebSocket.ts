/**
 * WebSocket hook
 */

export function useWebSocket(url: string) { return { connected: false, send: (_: any) => {} }; }

