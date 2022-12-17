from homework_1.task_4.task_4_functions import determine_x_and_y_ranges_by_dimension

def test_determine_x_and_y_ranges_by_dimension_1():
    # act
    actual_result:tuple[str,str] = determine_x_and_y_ranges_by_dimension(1)
    # assert
    assert actual_result == ("0 to ∞", "0 to ∞")

def test_determine_x_and_y_ranges_by_dimension_2():
    # act
    actual_result:tuple[str,str] = determine_x_and_y_ranges_by_dimension(2)
    # assert
    assert actual_result == ("0 to -∞", "0 to ∞")

def test_determine_x_and_y_ranges_by_dimension_3():
    # act
    actual_result:tuple[str,str] = determine_x_and_y_ranges_by_dimension(3)
    # assert
    assert actual_result == ("0 to -∞", "0 to -∞")

def test_determine_x_and_y_ranges_by_dimension_4():
    # act
    actual_result:tuple[str,str] = determine_x_and_y_ranges_by_dimension(4)
    # assert
    assert actual_result == ("0 to ∞", "0 to -∞")