# !/bin/bash

alembic upgrade head
PYTHONPATH=. uvicorn --factory user_service.main:create_app --host 0.0.0.0 --port 8000 --reload