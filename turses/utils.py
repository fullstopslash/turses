# -*- coding: utf-8 -*-

"""
This module contains functions used across different modules.
"""
import sys
from re import findall
from re import compile as compile_regex
from sys import stdout
from functools import partial


URL_REGEX = compile_regex('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|'
                          '(?:%[0-9a-fA-F][0-9a-fA-F]))+')


def matches_word(regex, word):
    """
    Return `True` if the whole `word` is matched by `regex`, `False`
    otherwise.
    """
    match = regex.match(word)
    if match:
        return match.start() == 0 and match.end() == len(word)
    return False


def sanitize_username(username):
    return ''.join(filter(is_username, username))


def prepend_at(username):
    return '@%s' % username


# username
username_regex = compile_regex(r'[A-Za-z0-9_]+')
is_username = partial(matches_word, username_regex)

# hashtag
hashtag_regex = compile_regex(r'#.+')
is_hashtag = partial(matches_word, hashtag_regex)

# URL
is_url = partial(matches_word, URL_REGEX)


def get_urls(text):
    return findall(URL_REGEX, text)


def encode(string):
    if sys.version_info < (3,):
        try:
            return string.encode(stdout.encoding, 'replace')
        except (AttributeError, TypeError):
            return string
    else:
        return string
