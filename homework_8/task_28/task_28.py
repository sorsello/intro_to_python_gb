# Создать информационную систему позволяющую работать с учениками школы
# функции
# Добавление нового студента (Поля - имя, фамилия)
# Добавление предмета (добавляется всем ученикам сразу)
# Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )
# Показ списка учеников (имена фамилия)
# Показ листа оценок конкретного ученика
# Выход из программы
# Достаточно хранить данные в переменной

from homework_8.task_28.console_command_service import display_available_options, capture_user_action_number
from homework_8.task_28.controller import run_the_application

dict_of_students = {}
while True:
    display_available_options()
    selected_action: int = capture_user_action_number()
    run_the_application(selected_action, dict_of_students)