# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from common.console_helpers import capture_user_input_number_float

user_input: float = capture_user_input_number_float("Please enter a precision float: ")
if user_input > 0.1 or user_input < 0.0000000001:
    print("Your input is outside of allowed boundaries - min: 0.0000000001 max: 0.1")
    exit()

try:
    index_of_comma: int = str(user_input).index(".")
    after_decimal: str = str(user_input)[index_of_comma+1:]
    round_degree: int = len(after_decimal)
except ValueError:
    index_of_comma: int = str(user_input).index("-")
    after_decimal: str = str(user_input)[index_of_comma + 1:]
    round_degree: int = int(after_decimal)

number_pi: float = math.pi
rounded_pi: float = round(number_pi, round_degree)
print(rounded_pi)