import pytest
import main

grade_boundaries = {
    'max': 350,
    'A*': 264,
    'A': 229,
    'B': 189,
    'C': 150,
    'D': 111,
    'E': 72,
    'U': 0

}


def test_normal_data():
    assert main.calc_grades(189, grade_boundaries) == 'B'


def test_above_max():
    with pytest.raises(ValueError):
        main.calc_grades(351, grade_boundaries)


def test_min_score():
    assert main.calc_grades(0, grade_boundaries) == 'U'



def test_max_score():
    assert main.calc_grades(350, grade_boundaries) == 'A*'


def test_negative_fail():
    with pytest.raises(ValueError):
        main.calc_grades(-1, grade_boundaries)



def test_wrong_type():
    with pytest.raises(TypeError):
        main.calc_grades('Apple', grade_boundaries)  # type: ignore
