/**
 * Hub API client
 */

export interface HubConfig {
  baseUrl: string;
  token?: string;
}

export class HubClient {
  private config: HubConfig;

  constructor(config: HubConfig) {
    this.config = config;
  }

  async listModels(query?: string): Promise<string[]> { return []; }
  async getModel(id: string): Promise<any> { return null; }
  async downloadModel(id: string, outDir: string): Promise<string> { return outDir; }
  async uploadModel(path: string, repoId: string): Promise<void> {}
}

