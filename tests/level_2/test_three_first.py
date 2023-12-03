import pytest
from functions.level_2.three_first import first


@pytest.mark.parametrize('items, default, expected',
                         [([1, 2, 3], 'some_default', 1),
                          ([1, 2, 3], None, 1)])
def test__first__success(items, default, expected):
    assert first(items, default) == expected


@pytest.mark.parametrize('items, default, expected',
                         [([], 'some_default', 'some_default'),
                          ([], None, None)])
def test__first__empty_list(items, default, expected):
    assert first(items, default) == expected


# @pytest.mark.parametrize('items, default, expected',
#                          [(123, 'some_default', TypeError),
#                           ([], 'NOT_SET', AttributeError)])
# def test__first__error(items, default, expected):
#     with pytest.raises(expected):
#         first(items, default)
#
