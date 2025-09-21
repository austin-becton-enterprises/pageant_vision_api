#!/bin/bash
# Usage: ./add_dummy_purchases_to_db.sh [--cleanup|--add-all-dummy-data --force]
export PYTHONPATH=.
python3 scripts/add_dummy_purchases.py "$@"
