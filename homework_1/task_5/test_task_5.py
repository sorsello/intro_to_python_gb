import pytest

from homework_1.task_5.task_5_functions import calc_distance_between_coord

@pytest.mark.parametrize('coordinates,expected_result', [
    ((3,6,2,1), 5.1),
    ((7,-5,1,-1), 7.21)
])
def test_determine_coordinates_dimension(coordinates, expected_result):
    # act
    actual_result:float = calc_distance_between_coord(coordinates)
    # assert
    assert actual_result == expected_result