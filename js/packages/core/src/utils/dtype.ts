/**
 * Data type utils
 */

export type DType = 'float32' | 'float16' | 'int32' | 'int8';
export function inferDtype(data: ArrayBufferView): DType { return 'float32'; }

