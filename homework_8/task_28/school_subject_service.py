from homework_8.task_28.console_command_service import print_lines_logic_break

def add_subject_to_all_students(dict_of_students, school_subject:str) -> None:
    if len(dict_of_students) == 0:
        print("The list of students is empty. Cannot add subject.")
        print_lines_logic_break()
    else:
        for key in dict_of_students:
            if dict_of_students[key].get(school_subject) != None:
                print(f"Student '{key}' already has the subject '{school_subject}'. Not added.")
                print_lines_logic_break()
            else:
                dict_of_students[key][school_subject] = []
                print(f"Student '{key}' has the subject added '{school_subject}'.")
                print_lines_logic_break()