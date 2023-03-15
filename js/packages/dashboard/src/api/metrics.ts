/**
 * Metrics API
 */

export interface Metric { name: string; value: number; step: number; timestamp: number; }
export function aggregateMetrics(metrics: Metric[]): Record<string, number> { return {}; }

