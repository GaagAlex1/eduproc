from fastapi import APIRouter, Depends
from sqlalchemy import select
from backend.auth.router import user_dependency
from backend.database import db_dependency
from backend.models.schemas import StudentBase, CourseBase, TeacherBase, TaskBase, LessonBase, SolutionBase
from backend.models.db_model import *

course_request_router = APIRouter(prefix='/course')


@course_request_router.get('/participant')
async def get_student_or_teacher_by_user_id(
        user: user_dependency,
        db: db_dependency
) -> StudentBase | TeacherBase | None:
    user_orm: User | None = await db.get(User, user.id)
    if user_orm is not None:
        student: Student = user_orm.student
        teacher: Teacher = user_orm.teacher
        if student is not None:
            return StudentBase.from_orm(student)
        elif teacher is not None:
            return TeacherBase.from_orm(teacher)


@course_request_router.get('/courses')
async def get_courses_by_participant(
        db: db_dependency,
        participant: StudentBase | TeacherBase | None = Depends(get_student_or_teacher_by_user_id)
) -> List[CourseBase] | None:
    part_orm: Student | Teacher | None = None
    if isinstance(participant, StudentBase):
        part_orm: Student = await db.get(Student, participant.id)
    elif isinstance(participant, TeacherBase):
        part_orm: Teacher = await db.get(Teacher, participant.id)
    if part_orm is not None:
        courses_orm: List[Course] = part_orm.courses
        courses: List[CourseBase] = [CourseBase.from_orm(course) for course in courses_orm]
        return courses


@course_request_router.get('/courses/{course_id}}/')
async def get_lessons_by_course(
        db: db_dependency,
        course_id: int
) -> List[LessonBase] | None:
    course_orm: Course | None = await db.get(Course, course_id)
    if course_orm is not None:
        lessons_orm: List[Lesson] = course_orm.lessons
        lessons: List[LessonBase] = [LessonBase.from_orm(lesson) for lesson in lessons_orm]
        return lessons


@course_request_router.get('/tasks')
async def get_tasks_by_lesson(
        db: db_dependency,
        lesson_id: int
) -> List[TaskBase] | None:
    lesson_orm: Lesson | None = await db.get(Lesson, lesson_id)
    if lesson_orm is not None:
        tasks_orm: List[Task] = lesson_orm.tasks
        tasks: List[TaskBase] = [TaskBase.from_orm(task) for task in tasks_orm]
        return tasks


@course_request_router.get('/task/{task_id}')
async def get_solutions_by_task_and_student(
        db: db_dependency,
        task_id: int,
        student: StudentBase | None = Depends(get_student_or_teacher_by_user_id)
) -> SolutionBase | None:
    task_orm: Task | None = await db.get(Task, task_id)
    if task_orm is not None:
        student_orm: Student | None = await db.get(Student, student.id)
        stmt = select(Solution).join(Team).filter(Solution.team.has(Team.students.contains(student_orm)))
        solution_orm: Solution = (await db.execute(stmt)).scalars().one()
        return SolutionBase.from_orm(solution_orm)


