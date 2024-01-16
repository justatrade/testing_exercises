import os

import pytest

from functions.level_4.five_extra_fields import fetch_app_config_field
from functions.level_4.five_extra_fields import fetch_extra_fields_configuration


@pytest.fixture(scope='session')
def create_config_file():
    config_file = 'config.txt'
    config = '''[tool:app-config]
    ServerAliveInterval = 45
    Compression = yes
    CompressionLevel = 9
    ForwardX11 = yes
    extra_fields = Port: 50022 
        some_extra_field: "Hell, yes!"'''
    with open(config_file, 'w') as file_handler:
        file_handler.write(config)

    yield config_file
    os.remove(config_file)


def test__fetch_app_config_field__success(create_config_file):
    assert fetch_app_config_field(create_config_file, 'Compression') == 'yes'
    assert fetch_app_config_field(create_config_file, 'ForwardX11') == 'yes'


def test__fetch_extra_fields_configuration__success(create_config_file):
    assert len(fetch_extra_fields_configuration(create_config_file)) == 2
