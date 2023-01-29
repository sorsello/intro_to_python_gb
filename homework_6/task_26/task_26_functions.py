def to_the_power_of(number:int, power_of:int) -> int:
    if power_of == 0:
        return 1

    if power_of >= 1:
        return number * to_the_power_of(number, power_of - 1)