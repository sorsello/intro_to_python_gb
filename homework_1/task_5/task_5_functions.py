import math

def calc_distance_between_coord(user_coordinates: tuple[int,int,int,int]) -> float:
    distance: float = math.sqrt((user_coordinates[2] - user_coordinates[0]) ** 2 + (user_coordinates[3] - user_coordinates[1]) ** 2)
    distance_rounded: float = round(distance, 2)
    return distance_rounded

def display_final_result(user_coordinates: tuple[int,int,int,int], result: float) -> None:
    print(f"A ({user_coordinates[0]}, {user_coordinates[1]}); B ({user_coordinates[2]}, {user_coordinates[3]}) -> {result}")