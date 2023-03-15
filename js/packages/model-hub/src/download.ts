/**
 * Model download
 */

export async function downloadModel(modelId: string, revision?: string): Promise<string> { return `/models/${modelId}`; }

