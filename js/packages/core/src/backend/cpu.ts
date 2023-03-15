/**
 * CPU backend
 */

export interface BackendOptions {
  device?: string;
  precision?: 'float32' | 'float16';
}

export class CPUBackend {
  private options: BackendOptions;

  constructor(options: BackendOptions = {}) {
    this.options = options;
  }

  async initialize(): Promise<void> { /* CPU init */ }
  isSupported(): boolean { return true; }
  getName(): string { return 'CPU'; }
  dispose(): void { /* cleanup */ }
}

