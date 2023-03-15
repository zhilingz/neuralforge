/**
 * Model loading and management
 */

import { Tensor } from './tensor';

export interface ModelConfig {
  inputShape: number[];
  outputShape: number[];
  weights?: Record<string, Tensor>;
}

export class Model {
  private config: ModelConfig;
  private weights: Map<string, Tensor> = new Map();

  constructor(config: ModelConfig) {
    this.config = config;
    if (config.weights) {
      Object.entries(config.weights).forEach(([k, v]) => this.weights.set(k, v));
    }
  }

  predict(input: Tensor): Tensor { return input; }
  getWeight(name: string): Tensor | undefined { return this.weights.get(name); }
  summary(): string { return JSON.stringify(this.config); }
}

