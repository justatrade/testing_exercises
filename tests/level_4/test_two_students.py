import pytest

from functions.level_4.two_students import get_student_by_tg_nickname
from functions.level_4.two_students import Student


@pytest.fixture
def make_students_list():
    def create_student(number=1):
        students_list = []
        for student in range(number):
            students_list.append(Student(f'Ivan {student}',
                                         'Ivanov',
                                         f'@ivan_ivanov{student}'))
        return students_list
    return create_student


@pytest.mark.parametrize('number_of_students, searched_student, expected',
                         [
                             (num := 5, f'ivan_ivanov{num - 1}', True),
                             (num := 3, f'petr_ivanov{num - 1}', False)
                         ])
def test__get_student_by_tg_nickname__success(number_of_students,
                                              searched_student,
                                              expected,
                                              make_students_list):
    students_list = make_students_list(number_of_students)
    result = get_student_by_tg_nickname(searched_student, students_list)
    if result:
        result = result.telegram_account[1:]

    assert (result == searched_student) == expected
    