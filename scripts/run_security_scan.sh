#!/bin/bash
set -e
semgrep scan --config .semgrep/
bandit -r python/neuralforge/
npm audit --prefix js/
