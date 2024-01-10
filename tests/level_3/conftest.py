import datetime
import decimal

import pytest

from functions.level_3.models import Expense, Currency, BankCard
from functions.level_3.models import ExpenseCategory


@pytest.fixture(scope='session')
def make_list_expenses():
    def create_expense(days=1, purchases=1, period=1, same_amount=0):
        expenses_list = []
        for day in range(1, days+1, period):
            day_spent = datetime.datetime.today() - datetime.timedelta(days=day)
            for purchase in range(1, purchases+1):
                if not same_amount:
                    amount = decimal.Decimal(sum(range(1, purchase+day)))
                else:
                    amount = decimal.Decimal(same_amount)
                expenses_list.append(
                    Expense(
                        amount=amount,
                        currency=Currency.USD,
                        card=BankCard(last_digits='1234', owner='Card Holder'),
                        spent_in='Some shop',
                        spent_at=day_spent,
                        category=None)
                )
        return expenses_list
    return create_expense


@pytest.fixture
def make_delimiter_combinations():
    def create_combination(word: str):
        combinations_list = []
        allowed_delimiters = {" ", ",", ".", "-", "/", "\\"}
        for left in allowed_delimiters:
            for right in allowed_delimiters:
                combinations_list.append(left + word + right)
            combinations_list.append(left + word)
            combinations_list.append(word + left)

        return combinations_list
    return create_combination


@pytest.fixture(scope='session')
def make_categorized_expenses(make_list_expenses):
    """
    Считаем общее число слов в триггер мапе, создаём список с инстансами класса Expense используемой ранее функцией
    make_list_expenses(). После чего, проходимся по всем элементам списка, и "пересоздаём" (т.к. датакласс неизменяемый,
    на основании текущего расхода такой же, но с указанием поля spent_in, которое проставляется из элементов triggers_map
    :param make_list_expenses:
    :return:
    """
    triggers_map = {
        ExpenseCategory.BAR_RESTAURANT: {"asador", "julis", "doc", "set", "bastard"},
        ExpenseCategory.SUPERMARKET: {"chinar", "sas", "green apple", "meat house", "clean house"},
        ExpenseCategory.ONLINE_SUBSCRIPTIONS: {"apple.com/bill", "leetcode.com", "zoom.us", "netflix"},
        ExpenseCategory.MEDICINE_PHARMACY: {"farm", "pharm", "alfa-pharm", "maname"},
        ExpenseCategory.THEATRES_MOVIES_CULTURE: {"tomsarkgh", "moscow cinema", "kino park", "cinema galleria"},
        ExpenseCategory.TRANSPORT: {"gg platform", "www.taxi.yandex.ru", "bolt.eu", "yandex go"},
    }
    triggers_amount = 0
    for each in triggers_map:
        triggers_amount += len(triggers_map[each])
    expenses_list = make_list_expenses(days=triggers_amount)
    i = 0
    for each in triggers_map:
        for item in triggers_map[each]:
            current_expense = expenses_list[i]
            new_expense = Expense(
                amount=current_expense.amount,
                currency=current_expense.currency,
                card=current_expense.card,
                spent_in=item,
                spent_at=current_expense.spent_at,
                category=current_expense.category
            )
            expenses_list[i] = new_expense
            i += 1

    return expenses_list
