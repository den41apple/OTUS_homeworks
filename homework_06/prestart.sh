#!/usr/bin/env bash

echo "Run migrations"
flask db upgrade

echo "Fill DB test data"
python fill_db_test_data.py
