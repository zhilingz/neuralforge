/**
 * Formatting utils
 */

export function formatNumber(n: number, decimals = 2): string { return n.toFixed(decimals); }
export function formatDuration(ms: number): string { return `${(ms / 1000).toFixed(1)}s`; }

