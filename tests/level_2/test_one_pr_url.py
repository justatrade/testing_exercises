import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url

# https://github.com/justatrade/crosses_and_zeros/pull/2


@pytest.mark.parametrize('url, expected',
                         [('https://github.com/justatrade/oop_bases_challenges/pull/3', True),
                          ('https://github.com/justatrade/crosses_and_zeros/pull/2', True)])
def test__is_github_pull_request_url__succses(url: str, expected: bool):
    assert is_github_pull_request_url(url) == expected


@pytest.mark.parametrize('url, expected',
                         [('https://pornhub.com/justatrade/oop_bases_challenges/pull/3', False),
                          ('https://github.com/justatrade/crosses_and_zeros/push/2', False),
                          ('https://////', False),
                          ('a/b/c/d/e/f', False),
                          ('', False)])
def test__is_github_pull_request_url__fail(url: str, expected: bool):
    assert is_github_pull_request_url(url) == expected


# @pytest.mark.parametrize('not_url, expected',
#                          [(12345, AttributeError),
#                           (123.45, AttributeError)])
# def test__is_github_pull_request_url__value_error(not_url: str, expected):  # не смог подобрать тут хинт, чтобы линтер не ругался
#     with pytest.raises(expected):
#         is_github_pull_request_url(not_url)
