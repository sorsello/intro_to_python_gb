# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона, комментрий
# - символ разделитель на выбор(можно использовать пробел или запятые) + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии

from homework_7.task_27.console_command_service import display_available_options, \
    capture_user_action_number
from homework_7.task_27.controller import run_the_application, enter_file_name

my_file_name: str = enter_file_name()
while True:
    display_available_options()
    selected_action: int = capture_user_action_number()
    if selected_action == 0:
        my_file_name = enter_file_name()
    run_the_application(selected_action, my_file_name)
