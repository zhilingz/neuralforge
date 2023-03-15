import { describe, it, expect } from 'vitest';
import { Tensor } from '../src';

describe('Tensor', () => {
  it('should be defined', () => {
    expect(Tensor).toBeDefined();
  });

  it('should initialize correctly', () => {
    const instance = new Tensor();
    expect(instance).toBeInstanceOf(Tensor);
  });
});
