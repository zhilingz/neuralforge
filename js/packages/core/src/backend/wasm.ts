/**
 * WASM backend
 */

export interface BackendOptions {
  device?: string;
  precision?: 'float32' | 'float16';
}

export class WasmBackend {
  private options: BackendOptions;

  constructor(options: BackendOptions = {}) {
    this.options = options;
  }

  async initialize(): Promise<void> { /* Wasm init */ }
  isSupported(): boolean { return true; }
  getName(): string { return 'Wasm'; }
  dispose(): void { /* cleanup */ }
}

