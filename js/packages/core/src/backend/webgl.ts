/**
 * WebGL backend
 */

export interface BackendOptions {
  device?: string;
  precision?: 'float32' | 'float16';
}

export class WebGLBackend {
  private options: BackendOptions;

  constructor(options: BackendOptions = {}) {
    this.options = options;
  }

  async initialize(): Promise<void> { /* WebGL init */ }
  isSupported(): boolean { return true; }
  getName(): string { return 'WebGL'; }
  dispose(): void { /* cleanup */ }
}

