import pytest
from main01 import get_rounded_number, get_word_count, get_ch_count_except_space


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 3),
        ("Python Family", 2),
    ],
)
def test_get_word_count(sentence, expected):
    assert get_word_count(sentence) == expected


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 10),
        ("Python Family", 12),
        ("Hello World", 10),
    ],
)
def test_get_ch_count_except_space(sentence, expected):
    assert get_ch_count_except_space("우리는 파이썬을 즐겨요") == 10
    assert get_ch_count_except_space("Python Famliy") == 12


@pytest.mark.parametrize(
    "digit, expected",
    [
        (12345, 12000),
        (987654, 987000),
        (9876, 9000),
    ],
)
def test_get_rounded_number(digit, expected):
    assert get_rounded_number(digit) == expected
