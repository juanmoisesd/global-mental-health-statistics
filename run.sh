#!/bin/bash
echo "Starting Global Mental Health Statistics Analysis..."
python3 scripts/etl/process_data.py
pytest tests/
