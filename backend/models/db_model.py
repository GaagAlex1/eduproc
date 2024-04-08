from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import List
from backend.database import Base


class Notification(Base):
    __tablename__ = 'notification'

    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[int]

    users: Mapped[List['User']] = relationship(back_populates='notifications',
                                               secondary='notification_user', lazy='selectin')


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    second_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[bytes]

    teacher: Mapped['Teacher'] = relationship('Teacher', back_populates='user', lazy='selectin')
    student: Mapped['Student'] = relationship('Student', back_populates='user', lazy='selectin')
    notifications: Mapped[List['Notification']] = relationship(back_populates='users',
                                                               secondary='notification_user', lazy='selectin')


class Course(Base):
    __tablename__ = 'course'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    students: Mapped[List['Student']] = relationship(back_populates='courses',
                                                     secondary='course_student', lazy='selectin')
    lessons: Mapped[List['Lesson']] = relationship('Lesson', back_populates='course', lazy='selectin')
    teachers: Mapped[List['Teacher']] = relationship(back_populates='courses',
                                                     secondary='course_teacher', lazy='selectin')


class Teacher(Base):
    __tablename__ = 'teacher'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped['User'] = relationship('User', back_populates='teacher', lazy='selectin')
    courses: Mapped[List['Course']] = relationship(back_populates='teachers',
                                                   secondary='course_teacher', lazy='selectin')


class Student(Base):
    __tablename__ = 'student'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    subgroup_id: Mapped[int] = mapped_column(ForeignKey('subgroup.id'))

    user: Mapped['User'] = relationship('User', back_populates='student', lazy='selectin')
    subgroup: Mapped['Subgroup'] = relationship('Subgroup', back_populates='students', lazy='selectin')
    teams: Mapped[List['Team']] = relationship(back_populates='students',
                                               secondary='team_student', lazy='selectin')
    lessons: Mapped[List['Lesson']] = relationship(back_populates='students',
                                                   secondary='lesson_student', lazy='selectin')
    courses: Mapped[List['Course']] = relationship(back_populates='students',
                                                   secondary='course_student', lazy='selectin')


class Group(Base):
    __tablename__ = 'group'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    subgroups: Mapped[List['Subgroup']] = relationship('Subgroup', back_populates='group', lazy='selectin')


class Subgroup(Base):
    __tablename__ = 'subgroup'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))

    group: Mapped['Group'] = relationship('Group', back_populates='subgroups', lazy='selectin')
    students: Mapped[List['Student']] = relationship('Student', back_populates='subgroup', lazy='selectin')
    lessons: Mapped[List['Lesson']] = relationship('Lesson', back_populates='subgroup', lazy='selectin')


class Lesson(Base):
    __tablename__ = 'lesson'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime]
    subgroup_id: Mapped[int] = mapped_column(ForeignKey('subgroup.id'))
    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'))

    course: Mapped['Course'] = relationship('Course', back_populates='lessons', lazy='selectin')
    subgroup: Mapped['Subgroup'] = relationship('Subgroup', back_populates='lessons', lazy='selectin')
    students: Mapped[List['Student']] = relationship(back_populates='lessons',
                                                     secondary='lesson_student', lazy='selectin')
    tasks: Mapped[List['Task']] = relationship('Task', back_populates='lesson', lazy='selectin')


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str]
    deadline: Mapped[datetime]
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lesson.id'))

    lesson: Mapped['Lesson'] = relationship('Lesson', back_populates='tasks', lazy='selectin')
    solutions: Mapped[List['Solution']] = relationship('Solution', back_populates='task', lazy='selectin')


class Team(Base):
    __tablename__ = 'team'

    id: Mapped[int] = mapped_column(primary_key=True)
    team_name: Mapped[str]

    students: Mapped[List['Student']] = relationship(back_populates='teams',
                                                     secondary='team_student', lazy='selectin')
    solutions: Mapped[List['Solution']] = relationship('Solution', back_populates='team', lazy='selectin')


class Solution(Base):
    __tablename__ = 'solution'

    id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str]
    pass_date: Mapped[datetime]
    mark: Mapped[int] = mapped_column(nullable=True)
    team_id: Mapped[int] = mapped_column(ForeignKey('team.id'))
    task_id: Mapped[int] = mapped_column(ForeignKey('task.id'))

    team: Mapped['Team'] = relationship('Team', back_populates='solutions', lazy='selectin')
    task: Mapped['Task'] = relationship('Task', back_populates='solutions', lazy='selectin')


class TeamStudent(Base):
    __tablename__ = 'team_student'

    team_id: Mapped[int] = mapped_column(ForeignKey('team.id'), primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'), primary_key=True)
    start_date: Mapped[datetime]
    end_date: Mapped[datetime] = mapped_column(nullable=True)


class LessonStudent(Base):
    __tablename__ = 'lesson_student'

    lesson_id: Mapped[int] = mapped_column(ForeignKey('lesson.id'), primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'), primary_key=True)


class CourseStudent(Base):
    __tablename__ = 'course_student'

    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'), primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id'), primary_key=True)


class CourseTeacher(Base):
    __tablename__ = 'course_teacher'

    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'), primary_key=True)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teacher.id'), primary_key=True)


class NotificationUser(Base):
    __tablename__ = 'notification_user'

    notification_id: Mapped[int] = mapped_column(ForeignKey('notification.id'), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
