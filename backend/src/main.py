from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from .db import DatabaseConnection

db = DatabaseConnection()

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield

app = FastAPI(lifespan=lifespan)

COURSES: list[dict[str, str|int]] = [
    {'id': 1, 'title': 'Numerical Methods', 'code': 'CSE330'},
    {'id': 2, 'title': 'Database Systems', 'code': 'CSE370'},
    {'id': 3, 'title': 'Artificial Intelligence', 'code': 'CSE422'},
]

@app.get('/')
async def index() -> dict[str, str]:
    return {
        'status': 'active'
    }

@app.get('/courses')
async def courses() -> list[dict[str, str|int]]:
    return COURSES

@app.get('/courses/{course_id}')
async def course(course_id: int) -> dict[str, str|int]:
    course = next((c for c in COURSES if c['id'] == course_id), None)

    if course is None:
        raise HTTPException(status_code=404, detail='Course not found')

    return course

def main():
    print("Hello from backend!")


if __name__ == "__main__":
    main()
