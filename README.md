# Okta RBAC Solution Architecture Demo

This Python project demonstrates capabilities expected from a Solution Architect and an IAM Engineer in a modern access control system.

## What this project shows

- Role-based access control (RBAC) model
- JWT validation and claims extraction
- Policy evaluation and enforcement
- Separation of architecture, integration, and implementation concerns
- Documentation of IAM and solution architecture responsibilities

## Project structure

- `src/` - core implementation of authentication, authorization, and policy models
- `docs/` - architecture and capability descriptions
- `tests/` - unit tests for key security flows

## Getting started

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the sample use case:
   ```bash
   python -m src.main
   ```

3. Run tests:
   ```bash
   pip install pytest
   pytest tests/test_auth.py
   ```

## Why this matters

A successful Solution Architect delivers a secure, scalable design and ensures the IAM Engineer can implement it reliably. This demo captures both roles by combining security patterns, architecture guidance, and runnable code.
