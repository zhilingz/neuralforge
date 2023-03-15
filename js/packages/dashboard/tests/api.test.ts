import { describe, it, expect } from 'vitest';
import { setupRoutes } from '../src';

describe('setupRoutes', () => {
  it('should be defined', () => {
    expect(setupRoutes).toBeDefined();
  });

  it('should initialize correctly', () => {
    const instance = new setupRoutes();
    expect(instance).toBeInstanceOf(setupRoutes);
  });
});
