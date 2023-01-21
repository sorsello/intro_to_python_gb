# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)

# Модуль восстановления работет в обратную сторону
# из строки выходных данных, получить строку входных данных.


from homework_5.task_23.task_23_functions import compress_string_rle, decompress_rle_numbers_or_letters

# my_input: str = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"
# initial_value_is_letters = True

my_input: str = "111112222334445"
initial_value_is_letters = False

print(f"Initial value -> {my_input}")
compressed_rle_string: str = compress_string_rle(my_input)
print(f"Compressed RLE string -> {compressed_rle_string}")

decompress_rle_numbers_or_letters(compressed_rle_string, initial_value_is_letters)

