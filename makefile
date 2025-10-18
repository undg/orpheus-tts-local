.PHONY: help install install-rocm run clean test run-lms

help:
	@echo "Available targets:"
	@echo "  install      - Install CPU version"
	@echo "  install-rocm - Install ROCm (AMD GPU) version"
	@echo "  run          - Run example.py"
	@echo "  run-lms      - Start lms server"
	@echo "  clean        - Remove cache and temp files"
	@echo "  test         - Run tests"

install:
	pip install -r requirements.txt

install-rocm:
	pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm7.0

run-lms:
	echo "You need to start GUI first (lmstudio)"
	lms server start
	lms load orpheus-3b-0.1-ft


run:
	python example.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete

test:
	python -m pytest

