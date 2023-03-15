/**
 * Cache management
 */

import * as os from 'os';
import * as path from 'path';
export function getCacheDir(): string { return path.join(os.homedir(), '.cache', 'neuralforge'); }

