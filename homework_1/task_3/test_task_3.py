import pytest

from homework_1.task_3.task_3_functions import determine_coordinates_dimension

@pytest.mark.parametrize('x,y,expected_dimension', [
    (34, -30, 4),
    (2, 4, 1),
    (-34, -30, 3),
    (-34, 27, 2),
])
def test_determine_coordinates_dimension(x, y, expected_dimension):
    # act
    actual_result:int = determine_coordinates_dimension(x, y)
    # assert
    assert actual_result == expected_dimension