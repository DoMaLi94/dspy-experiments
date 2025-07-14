#!/usr/bin/env bash
# Code formatting script for DSPy experiments

set -e

echo "🧹 Formatting code with pre-commit..."

echo "Running pre-commit hooks on all files..."
poetry run pre-commit run --all-files

echo "✅ Code formatting complete!"
