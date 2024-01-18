import pytest

from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.fixture
def string_with_brackets(test_string):
    yield '{"' + test_string + '"}'
    del test_string


@pytest.mark.parametrize('test_string, expected',
                         [
                             ('test_string', True),
                             ('""{}""', False)
                         ])
def test__delete_remove_brackets_quotes__success_fail(test_string,
                                                      expected,
                                                      string_with_brackets):
    result = (delete_remove_brackets_quotes(string_with_brackets) ==
              'test_string')
    assert result == expected
