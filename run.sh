#!/bin/bash
set -e
./install.sh
uvicorn main:app --host 0.0.0.0 --port 8000
