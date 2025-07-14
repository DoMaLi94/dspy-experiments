#!/usr/bin/env bash
# Code quality script for DSPy experiments

set -e

echo "🧹 Running code quality checks with pre-commit..."

echo "Running pre-commit hooks on all files (check mode)..."
poetry run pre-commit run --all-files --show-diff-on-failure

echo "✅ All code quality checks passed!"
