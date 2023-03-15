import { describe, it, expect } from 'vitest';
import { runCLI } from '../src';

describe('runCLI', () => {
  it('should be defined', () => {
    expect(runCLI).toBeDefined();
  });

  it('should initialize correctly', () => {
    const instance = new runCLI();
    expect(instance).toBeInstanceOf(runCLI);
  });
});
