import pytest

from homework_1.task_2.task2_functions import *

@pytest.mark.parametrize('index,current_list,expected_result', [
    (0, [0,0,0], [0,0,0]),
    (2, [0,0,0], [0,0,0]),
    (4, [0,0,0], [1,0,0]),
    (6, [1,0,0], [1,0,0]),
    (8, [1,0,0], [1,0,0]),
])
def test_set_one_to_the_second_half_values(index, current_list, expected_result):
    # act
    set_one_to_the_second_half_values(index, 8, current_list)
    # assert
    assert current_list == expected_result


@pytest.mark.parametrize('index,current_list,expected_result', [
    (0, [0,0,0], [0,0,1]),
    (1, [0,0,1], [0,0,0]),
    (4, [0,0,0], [0,0,1]),
    (5, [0,0,1], [0,0,0]),
])
def test_set_one_to_every_second_value(index, current_list, expected_result):
    # act
    set_one_to_every_second_value(index, current_list)
    # assert
    assert current_list == expected_result

@pytest.mark.parametrize('index,current_list,expected_result', [
    (0, [0,0,0], [0,1,0]),
    (1, [0,1,0], [0,1,0]),
    (2, [0,1,0], [0,0,0]),
    (3, [0,0,0], [0,0,0]),
    (4, [0,0,0], [0,1,0]),
])
def test_set_one_to_every_two_values(index, current_list, expected_result):
    # act
    set_one_to_every_two_values(index, current_list)
    # assert
    assert current_list == expected_result

def test_determine_true_or_false(test_data):
    assert determine_true_or_false(test_data) == True

@pytest.mark.parametrize('test_data', [[0, 1, 1], [0, 1, 0], [0, 0, 1],
                                       [0, 0, 0], [1, 1, 1], [1, 1, 0],
                                       [1, 0, 1], [1, 0, 0]])
def test_determine_true_or_false(test_data):
    assert determine_true_or_false(test_data) == True