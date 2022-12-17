def set_one_to_the_second_half_values(iteration_index:int, interations:int, current_list: list[int]) -> None:
    if(iteration_index >= interations/2 and current_list[0] == 0):
        current_list[0] = current_list[0] + 1
    else:
        pass

def set_one_to_every_two_values(iteration_index:int,current_list: list[int]) -> None:
    if(current_list[1] % 2 == 0 and iteration_index %2 == 0):
        current_list[1] = current_list[1] + 1
    elif(current_list[1] % 2 == 1 and iteration_index % 2 == 1):
        pass
    else:
        current_list[1] = 0

def set_one_to_every_second_value(iteration_index:int,current_list: list[int]) -> None:
    if (iteration_index % 2 == 0):
        current_list[2] = current_list[2] + 1
    else:
        current_list[2] = 0

def determine_true_or_false(generated_list:list[int]) -> bool:
    x: int = generated_list[0]
    y: int = generated_list[1]
    z: int = generated_list[2]

    left_result: bool = not (x or y or z)
    right_result2: bool = not x and not y and not z
    if left_result == right_result2:
        return True
    else:
        return False
