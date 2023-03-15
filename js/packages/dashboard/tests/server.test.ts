import { describe, it, expect } from 'vitest';
import { createServer } from '../src';

describe('createServer', () => {
  it('should be defined', () => {
    expect(createServer).toBeDefined();
  });

  it('should initialize correctly', () => {
    const instance = new createServer();
    expect(instance).toBeInstanceOf(createServer);
  });
});
