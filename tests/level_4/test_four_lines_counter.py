import os

import pytest

from functions.level_4.four_lines_counter import count_lines_in


@pytest.fixture
def filepath(request):
    path_to_file = f'my_test_file_{request.param}.txt'
    with open(path_to_file, 'w') as file_handler:
        file_handler.writelines([str(i)+'\n' for i in range(request.param)])

    yield path_to_file, request.param
    os.remove(path_to_file)


@pytest.mark.parametrize("filepath",
                         [
                             10,
                             100,
                             1000000
                         ],
                         indirect=True)
def test__count_lines_in__success(filepath):
    file_path, number = filepath
    assert count_lines_in(filepath=file_path) == number
