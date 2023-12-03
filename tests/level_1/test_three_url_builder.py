import pytest

from functions.level_1.three_url_builder import build_url


@pytest.fixture
def base_url_data():
    return {'base': 'some-url.com','relative': 'relative_part'}


@pytest.fixture
def url_data_params(base_url_data):
    return {'params': {'param1': 'value1', 'param2': 'value2'}}


def test_build_url(base_url_data):
    assert build_url(base_url_data['base'],
                     base_url_data['relative']) == \
           base_url_data['base']+'/'+base_url_data['relative']


def test_build_url_params(base_url_data: dict[str, str],
                          url_data_params: dict[str, dict:[str, str]]):
    assert build_url(base_url_data['base'],
                     base_url_data['relative'],
                     url_data_params['params']) == \
           'some-url.com/relative_part?param1=value1&param2=value2'
