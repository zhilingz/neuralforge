import { describe, it, expect } from 'vitest';
import { HubClient } from '../src';

describe('HubClient', () => {
  it('should be defined', () => {
    expect(HubClient).toBeDefined();
  });

  it('should initialize correctly', () => {
    const instance = new HubClient();
    expect(instance).toBeInstanceOf(HubClient);
  });
});
