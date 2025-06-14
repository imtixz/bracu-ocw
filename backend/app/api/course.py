from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.core.db import DatabaseConnection
from app.models import Department, CourseBase, Course

db = DatabaseConnection()

router = APIRouter(prefix="/course", tags=["course"])


@router.get("/")
async def courses(
    department: Department | None = None, session: Session = Depends(db.get_session)
) -> list[Course]:
    course_list = list(session.exec(select(Course)).all())

    if department:
        course_list = [
            c for c in course_list if c.department.value.lower() == department.value
        ]

    return course_list


@router.post("/")
async def create_course(
    course_data: CourseBase, session: Session = Depends(db.get_session)
) -> Course:
    course = Course(
        title=course_data.title,
        code=course_data.code,
        description=None,
        department=course_data.department,
    )
    session.add(course)

    session.commit()
    session.refresh(course)

    return course


@router.patch("/")
async def update_course():
    pass


@router.get("/resources")
async def get_course_resources():
    pass


@router.post("/resource")
async def add_course_resource():
    # adds a resource to the course
    pass


@router.delete("/resource")
async def remove_course_resource():
    # has to be a mod
    # should accept resource id or sth (along with type)
    pass
