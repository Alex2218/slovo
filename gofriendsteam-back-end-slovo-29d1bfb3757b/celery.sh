#!/usr/bin/env bash
celery worker -A slovo_backend --concurrency=2 --loglevel=INFO --beat -E

