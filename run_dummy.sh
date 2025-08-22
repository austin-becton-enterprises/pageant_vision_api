#!/bin/bash
export USE_DUMMY_DB=1
uvicorn main:app --reload --host 0.0.0.0 --port 8000
