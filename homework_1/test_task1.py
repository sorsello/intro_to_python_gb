import pytest as pytest
from homework_1.task_1_functions import determine_if_week_day

@pytest.mark.parametrize('test_data', [1, 2, 3, 4, 5])
def test_determine_if_week_day_false(test_data):
    assert determine_if_week_day(test_data) == False

@pytest.mark.parametrize('test_data', [6, 7])
def test_determine_if_week_day_true(test_data):
    assert determine_if_week_day(test_data) == True