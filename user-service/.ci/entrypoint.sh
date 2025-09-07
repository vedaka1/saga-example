# !/bin/bash

alembic upgrade head
uvicorn --factory main:create_app --host 0.0.0.0 --port 8000 --reload