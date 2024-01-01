import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def empty_classroom():
    return Classroom(teacher=Teacher("Professor Snape"), students=[], course_title="Potions")

@pytest.fixture
def classroom_with_students():
    students = [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]
    return Classroom(teacher=Teacher("Professor McGonagall"), students=students, course_title="Transfiguration")

def test_add_student(empty_classroom):
    empty_classroom.add_student(Student("Neville Longbottom"))
    assert len(empty_classroom.students) == 1

def test_add_student_raises_exception(classroom_with_students):
    # Add students until the classroom is full (more than 10 students)
    for _ in range(8):
        classroom_with_students.add_student(Student("Random Student"))
    with pytest.raises(TooManyStudents):
        classroom_with_students.add_student(Student("Draco Malfoy"))

def test_remove_student(classroom_with_students):
    classroom_with_students.remove_student("Harry Potter")
    assert len(classroom_with_students.students) == 2
    assert all(student.name != "Harry Potter" for student in classroom_with_students.students)

def test_change_teacher(empty_classroom):
    empty_classroom.change_teacher(Teacher("Professor Flitwick"))
    assert empty_classroom.teacher.name == "Professor Flitwick"

# You can add more tests based on your requirements and scenarios.
