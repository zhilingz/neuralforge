/**
 * Shape validation
 */

export function validateShape(shape: number[]): boolean { return shape.every(d => d > 0); }
export function computeStrides(shape: number[]): number[] { return shape; }

