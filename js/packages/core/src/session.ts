/**
 * Inference session
 */

import { Model, ModelConfig } from './model';
import { Tensor } from './tensor';

export class InferenceSession {
  private model: Model;
  private initialized = false;

  constructor(config: ModelConfig) {
    this.model = new Model(config);
  }

  async initialize(): Promise<void> { this.initialized = true; }
  run(inputs: Record<string, Tensor>): Record<string, Tensor> {
    if (!this.initialized) throw new Error('Session not initialized');
    return { output: this.model.predict(Object.values(inputs)[0]) };
  }
  dispose(): void { this.initialized = false; }
}

