/**
 * Dashboard HTTP server
 */

import express from 'express';
import { setupRoutes } from './api';

export interface ServerConfig {
  port: number;
  host?: string;
}

export function createServer(config: ServerConfig) {
  const app = express();
  app.use(express.json());
  setupRoutes(app);
  return app.listen(config.port, config.host || '0.0.0.0');
}

