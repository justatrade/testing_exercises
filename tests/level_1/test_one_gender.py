import pytest

from functions.level_1.one_gender import genderalize


@pytest.fixture
def base_gender_data():
    return {'male': 'He goes','female': 'She goes', 'sex': 'male'}


def test_genderalize_male(base_gender_data):
    assert genderalize(base_gender_data['male'],
                       base_gender_data['female'],
                       base_gender_data['sex']) == base_gender_data['male']


def test_genderalize_female(base_gender_data):
    assert genderalize(base_gender_data['male'],
                       base_gender_data['female'],
                       'female') == base_gender_data['female']


def test_return_type():
    assert type(genderalize('goes', 'goes', 'male') == type(str))
