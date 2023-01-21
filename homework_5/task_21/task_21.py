# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)


target_match: str = "абв"
text: str = "освоение. #@ мавбаваывбывабврса! в , авыавы ыв авы! абв ? вбвавб  вабва б аввб "

my_list: list[str] = text.split()

final_list: list[str] = [x for x in my_list if target_match not in x]
final_string: str = ' '.join(final_list)

print(final_string)