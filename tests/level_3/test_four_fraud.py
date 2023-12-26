import pytest

from functions.level_3.four_fraud import find_fraud_expenses


@pytest.mark.parametrize('days, purchases, same_amount, expected',
                         [
                             (1, 1, 1000, False),
                             (2, 1, 10000, False),
                             (1, 4, 10000, False),
                             (1, 4, 1000, True),
                             (2, 5, 4999, True)
                         ])
def test__find_fraud_expenses__success_fail(days, purchases, same_amount,
                                            expected, make_list_expenses):
    list_expenses = make_list_expenses(days=days,
                                       purchases=purchases,
                                       period=1,
                                       same_amount=same_amount)
    fraud_expenses_count = len(find_fraud_expenses(list_expenses))

    assert (fraud_expenses_count > 0) == expected
