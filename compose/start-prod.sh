#!/bin/bash

set -o errexit
set -o nounset


uvicorn --host 0.0.0.0 --port 8000 src.fastapi_app:app
