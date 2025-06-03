alembic commands

alembic init migrations
alembic revision --autogenerate
alembic upgrade head

start project with
uvicorn src.main:app