from app.main import get_human_age


def test_should_return_zero_when_both_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_ages_are_less_than_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_are_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_two_when_ages_are_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_convert_cat_age_after_twenty_four() -> None:
    assert get_human_age(28, 24) == [3, 2]


def test_should_convert_dog_age_after_twenty_four() -> None:
    assert get_human_age(24, 29) == [2, 3]


def test_should_return_correct_human_age_for_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
