from homework_8.task_28.console_command_service import print_lines_logic_break

def add_student(dict_of_students, first_name:str, last_name:str) -> None:
    student_first_last_name: str = f"{first_name} {last_name}"
    if dict_of_students.get(student_first_last_name) != None:
        print(f"The student '{student_first_last_name}' already exists. Cannot have duplicates.")
        print_lines_logic_break()
    else:
        dict_of_students[student_first_last_name] = {}
        print(f"The student '{student_first_last_name}' has been added.")

def display_all_students_first_last_name(dict_of_students) -> None:
    if len(dict_of_students) == 0:
        print("The list of students is empty. Nothing to display.")
    else:
        for key in dict_of_students:
            print(key)
        print_lines_logic_break()