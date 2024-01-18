import pytest
import unittest.mock

from functions.level_4.three_promocodes import generate_promocode


def return_letter(letter: str):
    return letter


@pytest.mark.parametrize("letter, number, expected",
                         [
                             ('B', 3, 'BBB'),
                             ('A', 10, 'AAAAAAAAAA')
                         ])
def test__generate_promocode__moked(letter: str,
                                    number: int, expected: str):
    mocked_part = 'functions.level_4.three_promocodes.string.ascii_uppercase'
    with unittest.mock.patch(mocked_part,
                             new=return_letter(letter)) as mocked_letter:
        assert generate_promocode(number) == expected

