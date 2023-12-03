import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize('text, good_words, bad_words, expected',
                         [('Bright sun is shining',
                           {'bright', 'shining'},
                           {'fuck', 'shit'},
                           'GOOD'),
                          ('Bright fuck is shit',
                           {'bright', 'shining'},
                           {'fuck', 'shit'},
                           'BAD')])
def test__check_tweet_sentiment__success(text: str, good_words: set[str],
                                         bad_words: set[str], expected: str):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected


@pytest.mark.parametrize('text, good_words, bad_words, expected',
                         [('Bright sun is shining',
                           set(),
                           set(),
                           None),
                          ('Bright fuck is shit',
                           {'bright', 'shining'},
                           {'bright', 'shining'},
                           None)])
def test__check_tweet_sentiment__fail(text: str, good_words: set[str],
                                      bad_words: set[str], expected: None):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected


# @pytest.mark.parametrize('text, good_words, bad_words, expected',
#                          [(123, set(), set(), AttributeError)])
# def test__check_tweet_sentiment__error(text: str, good_words: set[str],
#                                        bad_words:set[str], expected):
#     with pytest.raises(expected):
#         check_tweet_sentiment(text, good_words, bad_words)
