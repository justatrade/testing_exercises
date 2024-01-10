import decimal

import pytest

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


@pytest.mark.parametrize('fixt_params, expected',
                         [({'days': 1, 'purchases': 1},
                           decimal.Decimal('1')),
                          ({'days': 3, 'purchases': 5},
                           decimal.Decimal('56.66666666666666666666666667')),
                          ({'days': 100, 'purchases': 11},
                           decimal.Decimal('21884.5'))])
def test__calculate_average_daily_expenses__success(fixt_params,
                                                    expected,
                                                    make_list_expenses):
    expenses_list = make_list_expenses(days=fixt_params['days'],
                                       purchases=fixt_params['purchases'])
    assert calculate_average_daily_expenses(
        expenses_list
    ) == expected
    