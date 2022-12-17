# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
from common import console_helpers
from homework_1.task_1_functions import determine_if_week_day

user_input = input("Enter a day of the week number: ")
try:
    user_input_int: int = int(user_input)
except ValueError:
    console_helpers.exit_program_with_error_message("The input must be a number.")

if user_input_int >= 1 and user_input_int <= 7:
    result: bool = determine_if_week_day(user_input_int)
    print(result)
else:
    console_helpers.exit_program_with_error_message("The input number is greater than 7 or less than 1.")