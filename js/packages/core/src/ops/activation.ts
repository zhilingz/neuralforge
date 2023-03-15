/**
 * Activation ops
 */

export function relu(x: Float32Array): Float32Array { return x.map(v => Math.max(0, v)) as unknown as Float32Array; }
export function sigmoid(x: Float32Array): Float32Array { return x; }

