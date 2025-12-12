#!/usr/bin/env bash

set -e  # corta si hay errores

# Activar entorno virtual
source .venv/bin/activate

# Levantar la API
python -m uvicorn app.main:app --reload
