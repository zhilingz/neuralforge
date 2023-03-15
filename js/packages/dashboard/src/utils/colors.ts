/**
 * Color palette
 */

export const COLORS = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f'];
export function getColor(index: number): string { return COLORS[index % COLORS.length]; }

