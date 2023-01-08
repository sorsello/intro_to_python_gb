# Напишите программу,
# которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from common.console_helpers import capture_user_input_number

user_input: int = capture_user_input_number("Please enter a number: ")
binary_result: str = bin(user_input)

if user_input > 0:
    stripped_result: str = binary_result.strip("0b")
else:
    stripped_result: str = binary_result.strip("-0b")

print(stripped_result)