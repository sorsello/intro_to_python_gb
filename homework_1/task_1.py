# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def determine_if_week_day(user_number: int) -> bool:
    if user_number >= 1 and user_number <= 5:
        return False
    else:
        return True


user_input = input("Enter a day of the week number: ")
try:
    user_input_int: int = int(user_input)
except ValueError:
    print("The input must be a number. The program will exit now.")
    exit()

if user_input_int >= 1 and user_input_int <= 7:
    result: bool = determine_if_week_day(user_input_int)
    print(result)
else:
    print("The input number is greater than 7 or less than 1. The program will exit now.")
    exit()
