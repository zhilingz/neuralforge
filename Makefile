.PHONY: lint test build publish-pypi publish-npm security clean

lint:
	ruff check python/
	cd js && npm run lint

test:
	pytest python/tests/ -v
	cd js && npm test

build:
	cd python && python -m build
	cd js && npm run build

publish-pypi:
	twine upload python/dist/*

publish-npm:
	cd js && npm publish --workspaces --access public

security:
	semgrep scan --config .semgrep/
	bandit -r python/neuralforge/ -c .bandit
	cd js && npm audit

clean:
	rm -rf python/dist python/build python/*.egg-info
	rm -rf js/packages/*/dist
	find . -type d -name __pycache__ -exec rm -rf {} +
