from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class StudentBase(BaseModel):
    id: int
    subgroup_id: int

    class Config:
        from_attributes = True


class TeacherBase(BaseModel):
    id: int

    class Config:
        from_attributes = True


class CourseBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    id: int
    subject: str
    deadline: datetime

    class Config:
        from_attributes = True


class SolutionBase(BaseModel):
    id: int
    link: str
    pass_date: datetime
    mark: Optional[int]
    task_id: int
    team_id: int

    class Config:
        from_attributes = True


class TeamBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class LessonBase(BaseModel):
    id: int
    date: datetime
    subgroup_id: int
    course_id: int

    class Config:
        from_attributes = True
