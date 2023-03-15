/**
 * Tensor implementation
 */

export type DType = 'float32' | 'float16' | 'int32';

export class Tensor {
  readonly data: Float32Array;
  readonly shape: number[];
  readonly dtype: DType;

  constructor(data: Float32Array | number[], shape?: number[], dtype: DType = 'float32') {
    this.data = data instanceof Float32Array ? data : new Float32Array(data);
    this.shape = shape || [this.data.length];
    this.dtype = dtype;
  }

  get size(): number { return this.data.length; }
  reshape(newShape: number[]): Tensor { return new Tensor(this.data, newShape, this.dtype); }
  slice(start: number, end: number): Tensor { return new Tensor(this.data.slice(start, end)); }
  clone(): Tensor { return new Tensor(new Float32Array(this.data), [...this.shape], this.dtype); }
}

