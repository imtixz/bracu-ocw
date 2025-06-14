from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Department(Enum):
    BUSINESS = "business"
    COMPUTER_SCIENCE_ENGINEERING = "cse"
    MATHS = "mns/maths"
    PHYSICS = "mns/physics"
    BIOTECHNOLOGY = "mns/biotechnology"
    MICROBIOLOGY = "mns/microbiology"
    ELECTRICAL_ENGINEERING = "eee"
    LAW = "law"
    PHARMACY = "pharmacy"
    ARCHITECTURE = "architecture"
    ECONOMICS = "economics"
    ENGLISH = "english"
    GENERAL_EDUCATION = "gened"


class SemesterSeason(Enum):
    SPRING = "spring"
    SUMMER = "summer"
    FALL = "fall"


class CourseBase(SQLModel):
    title: str
    code: str
    description: Optional[str]
    department: Department


class Course(CourseBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tags: list["Tag"] = Relationship(back_populates="course")
    documents: list["Document"] = Relationship(back_populates="course")
    pair_documents: list["PairDocument"] = Relationship(back_populates="course")


class CourseCreate(CourseBase):
    pass


class TagBase(SQLModel):
    name: str


class Tag(TagBase):
    id: int | None = Field(default=None, primary_key=True)
    course: Course = Relationship(back_populates="tags")


class DocumentType(Enum):
    OUTLINE = "outline"
    READING = "reading"
    BOOK = "book"
    SLIDES = "slides"


class DocumentBase(SQLModel):
    filename: str
    filepath: str
    description: str
    type: DocumentType
    section: Optional[int]
    s_season: Optional[SemesterSeason]
    s_year: Optional[int]
    course_id: int = Field(foreign_key="course.id")


class Document(DocumentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course: Course = Relationship(back_populates="documents")


class PairDocumentType(Enum):
    PROBLEM_SET = "problem-set"
    ASSIGNMENT = "assignment"
    QUIZ = "quiz"
    MID = "mid"
    FINAL = "final"


class PairDocumentBase(SQLModel):
    q_filename: str
    q_filepath: str
    a_filename: Optional[str]
    a_filepath: Optional[str]
    description: str
    type: DocumentType
    section: Optional[int]
    s_season: SemesterSeason
    s_year: int
    course_id: int = Field(foreign_key="course.id")


class PairDocument(PairDocumentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course: Course = Relationship(back_populates="pair_documents")
