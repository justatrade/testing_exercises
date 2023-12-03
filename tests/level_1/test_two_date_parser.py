import datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.fixture
def base_date():
    return {'day': 'today', 'time': '04:20'}


@pytest.fixture
def future_date():
    return {'day': 'tomorrow', 'time': '12:00'}


@pytest.fixture
def wrong_data():
    return {'day': '123456','time': 'asdfghjkl'}


def test_compose_datetime_from(base_date):
    date = datetime.date.today()
    assert compose_datetime_from(base_date['day'],
                                 base_date['time']) == datetime.datetime(date.year,
                                                                    date.month,
                                                                    date.day,
                                                                    int('04'),
                                                                    int('20'))


def test_compose_datetime_tomorrow(future_date):
    date = datetime.date.today()
    full_date = datetime.datetime(date.year,
                                  date.month,
                                  date.day,
                                  int('12'),
                                  int('00'))
    assert compose_datetime_from(future_date['day'],
                                 future_date['time']) - full_date == \
           datetime.timedelta(days=1)


def test_compose_datetime_wrong_data(wrong_data):
    with pytest.raises(ValueError):
        compose_datetime_from(wrong_data['day'], wrong_data['time'])
