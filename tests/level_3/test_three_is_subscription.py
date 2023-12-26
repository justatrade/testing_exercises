import pytest

from functions.level_3.three_is_subscription import is_subscription


@pytest.mark.parametrize('days, period, expected',
                         [
                             (61, 30, True),
                             (60, 30, False),
                             (10, 1, False)
                         ])
def test__is_subscription__success_fale(days, period, expected,
                                        make_list_expenses):
    expenses_list = make_list_expenses(days=days, purchases=1, period=period)
    assert is_subscription(expenses_list[0], expenses_list) == expected
