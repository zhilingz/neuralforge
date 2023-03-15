/**
 * API routes
 */

import { Router, Application } from 'express';

export function setupRoutes(app: Application): void {
  const router = Router();
  router.get('/api/metrics', (req, res) => res.json({ metrics: [] }));
  router.get('/api/experiments', (req, res) => res.json({ experiments: [] }));
  router.get('/api/health', (req, res) => res.json({ status: 'ok' }));
  app.use(router);
}

