from text import (
    calculate_levenshtein_distance,
    clean_stop_word,
    clean_text,
    clean_word,
    get_distances_of_permutations,
    get_levensthein_distance_for_single_word,
    get_permutations_of_words,
    lowercase_each_arg,
    remove_non_alpha,
    split_text_by_whitespace_and_dash
)


def test_split_text_by_whitespace_and_dash():

    assert split_text_by_whitespace_and_dash("Nicola-Yarred, Master. Elias") == ['Nicola', 'Yarred,', 'Master.', 'Elias']


def test_calculate_levenshtein_distance_ignores_case():

    assert calculate_levenshtein_distance('aaab', 'aaB') == 1


def test_text_remove_non_alpha():
    input_text = "Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)"
    words_list = split_text_by_whitespace_and_dash(input_text)
    assert " ".join([remove_non_alpha(word) for word in words_list]) == "Potter Mrs Thomas Jr Lily Alexenia Wilson"


def test_clean_stop_word():
    input_text = "Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)"
    words_list = split_text_by_whitespace_and_dash(input_text)
    assert " ".join([clean_stop_word(word) for word in words_list]) == "Potter,  Thomas  (Lily Alexenia Wilson)"


def test_clean_word():
    assert clean_word("(Lily") == "Lily"
    input_text = "Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)"
    words_list = split_text_by_whitespace_and_dash(input_text)
    assert " ".join([clean_word(word) for word in words_list]) == "Potter  Thomas  Lily Alexenia Wilson"


def test_clean_text():
    input_text = "Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)"
    assert clean_text(input_text) == "potter thomas lily alexenia wilson"


def test_get_permutations_of_words():
    input = "Andersen-Jensen"
    assert get_permutations_of_words(input) == [('Andersen', 'Jensen'),('Jensen', 'Andersen')]


def test_get_distances_of_permutations():
    text = "Andersen-Jensen, Miss. Carla Christine Nielsine"
    search_query = "Jensen Andersen"

    assert get_distances_of_permutations(text=text, search_query=search_query) == [28, 25]


def test_get_levensthein_distance_for_single_word():
    text = "Andersen-Jensen, Miss. Carla Christine Nielsine"
    search_query = "Andersen"

    assert get_levensthein_distance_for_single_word(text=text, search_query=search_query) == [1e-05, 8.00002, 21.00003, 32.00004, 25.000049999999998]


def test_lower_case_wrapper_single_arg():

    @lowercase_each_arg
    def foo(bar):
        return bar

    assert foo("AbAb") == "abab"


def test_lower_case_wrapper_multiple_arg():

    @lowercase_each_arg
    def foo(bar1, bar2):
        return bar1, bar2

    assert foo("AbAb", "bAAb") == ("abab", "baab")
