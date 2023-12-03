import pytest
from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize('text, word_from, word_to, expected',
                         [('one two', 'one', 'three', 'three two'),
                          ('THREE FIVE', 'three', 'six', 'six FIVE')])
def test__replace_word__success(text, word_from, word_to, expected):
    assert replace_word(text, word_from, word_to) == expected


@pytest.mark.parametrize('text, word_from, word_to, expected',
                         [('one two', 'four', 'three', 'one two'),
                          ('THREE FIVE', 'four', 'six', 'THREE FIVE')])
def test__replace_word__fail(text, word_from, word_to, expected):
    assert replace_word(text, word_from, word_to) == expected


# @pytest.mark.parametrize('text, word_from, word_to, expected',
#                          [(1, 'four', 'three', AttributeError),
#                           ([1, 2], 'four', 'six', AttributeError)])
# def test__replace_word__error(text: str, word_from, word_to, expected):
#     with pytest.raises(expected):
#         replace_word(text, word_from, word_to)