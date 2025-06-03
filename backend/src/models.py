from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field

class SemesterSeason(Enum):
    SPRING = 'spring'
    SUMMER = 'summer'
    FALL = 'fall'

class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    code: str

class DocumentType(Enum):
    OUTLINE = 'outline'
    READING = 'reading'
    BOOK = 'book'
    SLIDES = 'slides'

class Document(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    filename: str
    filepath: str
    description: str
    type: DocumentType
    section: Optional[int]
    s_season: Optional[SemesterSeason]
    s_year: Optional[int]

class PairDocumentType(Enum):
    PROBLEM_SET = 'problem-set'
    ASSIGNMENT = 'assignment'
    QUIZ = 'quiz'
    MID = 'mid'
    FINAL = 'final'

class PairDocument(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    q_filename: str
    q_filepath: str
    a_filename: Optional[str]
    a_filepath: Optional[str]
    description: str
    type: DocumentType
    section: Optional[int]
    s_season: SemesterSeason
    s_year: int
