import { describe, it, expect } from 'vitest';
import { add } from '../src';

describe('add', () => {
  it('should be defined', () => {
    expect(add).toBeDefined();
  });

  it('should initialize correctly', () => {
    const instance = new add();
    expect(instance).toBeInstanceOf(add);
  });
});
