/**
 * Experiments API
 */

export interface Experiment { id: string; name: string; status: 'running' | 'completed' | 'failed'; }
export function listExperiments(): Experiment[] { return []; }

