import { describe, it, expect } from 'vitest';
import { Model } from '../src';

describe('Model', () => {
  it('should be defined', () => {
    expect(Model).toBeDefined();
  });

  it('should initialize correctly', () => {
    const instance = new Model();
    expect(instance).toBeInstanceOf(Model);
  });
});
