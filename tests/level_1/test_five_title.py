import pytest

from functions.level_1.five_title import change_copy_item


@pytest.fixture
def base_book():
    return {'name': 'Some book name (1234)', 'max_l': 20}


@pytest.fixture
def base_copy_book(base_book):
    return {'name': 'Copy of ' + base_book['name'], 'max_l': 100}


def test_change_copy_item(base_book: dict[str, str | int]):
    assert change_copy_item(base_book['name'],
                            base_book['max_l']) == 'Some book name (1234)'


def test_change_copy_long_item(base_book: dict[str, str | int]):
    assert change_copy_item(base_book['name'], 100) == 'Copy of Some book name (1234)'


def test_change_copy_item_number(base_copy_book: dict[str, str | int]):
    assert change_copy_item(base_copy_book['name'], base_copy_book['max_l']) ==\
           'Copy of Some book name (1235)'


@pytest.mark.parametrize('name, max_l, expected',
                         [
                             ('Book name 1 (1234)',
                              50,
                              'Copy of Book name 1 (1234)'),
                             ('Veeeeeery long book name (1234)',
                              15,
                              'Veeeeeery long book name (1234)')
                         ])
def test_several_items(name, max_l, expected):
    assert change_copy_item(name, max_l) == expected
