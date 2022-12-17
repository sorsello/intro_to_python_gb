from common.console_helpers import exit_program_with_error_message

def determine_coordinates_dimension(x:int, y:int) -> int:
    result: int
    if (x > 0 and y > 0):
        result = 1
    elif (x < 0 and y > 0):
        result = 2
    elif (x < 0 and y < 0):
        result = 3
    elif (x > 0 and y < 0):
        result = 4
    return result

def check_x_and_y_are_not_zero(x: int, y: int):
    if (x == 0):
        exit_program_with_error_message(f"X is equal to 0.")
    if (y == 0):
        exit_program_with_error_message(f"Y is equal to 0.")

def display_final_result(x:int, y:int, dimension:int):
    print(f"x={x}; y={y} -> {dimension}")