import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import is_string_contains_trigger
from functions.level_3.two_expense_categorizer import guess_expense_category


@pytest.mark.parametrize('word, expected',
                         [
                             ('test', True),
                             ('..test..', True)
                         ])
def test__is_string_contains_trigger__success(make_delimiter_combinations, word, expected):
    word_combinations = make_delimiter_combinations(word=word)
    for each in word_combinations:
        assert is_string_contains_trigger(each, word) == expected


def test__guess_expense_category__success(make_categorized_expenses):
    expenses_list = make_categorized_expenses
    triggers_map = {
        ExpenseCategory.BAR_RESTAURANT: {"asador", "julis", "doc", "set", "bastard"},
        ExpenseCategory.SUPERMARKET: {"chinar", "sas", "green apple", "meat house", "clean house"},
        ExpenseCategory.ONLINE_SUBSCRIPTIONS: {"apple.com/bill", "leetcode.com", "zoom.us", "netflix"},
        ExpenseCategory.MEDICINE_PHARMACY: {"farm", "pharm", "alfa-pharm", "maname"},
        ExpenseCategory.THEATRES_MOVIES_CULTURE: {"tomsarkgh", "moscow cinema", "kino park", "cinema galleria"},
        ExpenseCategory.TRANSPORT: {"gg platform", "www.taxi.yandex.ru", "bolt.eu", "yandex go"},
    }
    for expense in expenses_list:
        assert expense.spent_in in triggers_map[guess_expense_category(expense)]
