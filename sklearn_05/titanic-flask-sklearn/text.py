import re
from itertools import permutations

import Levenshtein

STOP_WORDS_NAME = [
    'mr',
    'master',
    'mrs',
    'miss',
    'jr',
]


def ensure_cleaned_text_input(fun):
    def wrapper(*args, **kwargs):
        kwargs.update({
            'text': clean_text(kwargs.get('text')),
            'search_query': clean_text(kwargs.get('search_query'))
        })
        return fun(*args, **kwargs)
    return wrapper


def lowercase_each_arg(fun):
    def wrapper(*args, **kwargs):
        lowered_args = []
        for arg in args:
            lowered_args.append(arg.lower())
        return fun(*lowered_args, **kwargs)
    return wrapper


def split_text_by_whitespace_and_dash(text):
    """splits by ` ` and `-`"""
    return re.split("-|\\s", text)


@lowercase_each_arg
def calculate_levenshtein_distance(value1, value2):
    """ calculates Levenshtein distance between two strings
    https://en.wikipedia.org/wiki/Levenshtein_distance
    :param value1:
    :param value2:
    :return:
    """
    return Levenshtein.distance(value1, value2)


def remove_non_alpha(word):
    """get rid of anything else than a-z"""
    return "".join([char for char in word if char.isalpha()])


def clean_stop_word(word):
    """get rid of words making informational noise"""
    if remove_non_alpha(word).lower() not in STOP_WORDS_NAME:
        return word
    else:
        return ""


def clean_word(word):
    """performs single word cleaning"""
    return clean_stop_word(remove_non_alpha(word))


@lowercase_each_arg
def clean_text(text):
    """splits text and perform clean_word on each word and joins back"""
    return " ".join([clean_word(word) for word
                     in split_text_by_whitespace_and_dash(text)
                     if clean_word(word)])


def get_permutations_of_words(text):
    """generate list of possible word permutations"""
    return list(permutations(split_text_by_whitespace_and_dash(text)))


@ensure_cleaned_text_input
def get_distances_of_permutations(text, search_query):
    """generate list of distances from text to each of words permutation generated from given in search_query name"""
    return [calculate_levenshtein_distance(text, " ".join(permutation))
            for permutation in get_permutations_of_words(search_query)]


@ensure_cleaned_text_input
def find_minimum_levenshtein_distance_among_word_permutations(text, search_query):
    """find smallest distance among all the permutations"""
    return min(get_distances_of_permutations(text=text, search_query=search_query))


@ensure_cleaned_text_input
def get_levensthein_distance_for_single_word(text, search_query):
    """return list of distances between search_query word and each of words in text assuming the importance of each
    consecutive word is decreasing (let's make the levensthein distance even bigger by multiplying it by enumerate)
    we add small number to calculated distance to avoid multiplication by zero results in same result when full match
    on further places"""
    return [(calculate_levenshtein_distance(value1=word, value2=search_query) + 0.00001) * (i + 1)
            for i, word in enumerate(split_text_by_whitespace_and_dash(text))]


@ensure_cleaned_text_input
def get_minimum_levensthein_distance_for_single_word(text, search_query):
    """find smallest distance from search_query to each of the text words"""
    return min(get_levensthein_distance_for_single_word(text=text, search_query=search_query))
