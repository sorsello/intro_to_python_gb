from homework_8.task_28.console_command_service import print_lines_logic_break

def add_grade_to_student_one_subject(dict_of_students, first_name:str, last_name:str,
                                     school_subject: str, grade:int) -> None:
    if len(dict_of_students) == 0:
        print("The list of students is empty. Cannot add grades.")
    else:
        student_first_last_name: str = f"{first_name} {last_name}"

        if dict_of_students.get(student_first_last_name) != None:
            if dict_of_students[student_first_last_name].get(school_subject) != None:
                if grade < 1 or grade > 5:
                    print(f"The grade cannot be less than 1 or greater than 5. The grade you entered '{grade}'")
                    print_lines_logic_break()
                else:
                    dict_of_students[student_first_last_name][school_subject].append(grade)
                    print(
                    f"The student '{student_first_last_name}' : added the grade '{grade}' for '{school_subject}'")
                    print_lines_logic_break()
            else:
                print(f"The student '{student_first_last_name}' does not have the subject '{school_subject}'. Cannot add grades.")
                print_lines_logic_break()
        else:
            print(f"The student '{student_first_last_name}' does not exist. Cannot add grades.")
            print_lines_logic_break()

def display_all_grades_for_student(dict_of_students, first_name:str, last_name:str) -> None:

    if len(dict_of_students) == 0:
        print("The list of students is empty. No grades to display.")
    else:
        student_first_last_name: str = f"{first_name} {last_name}"
        print(f"The student '{student_first_last_name}' has the following grades:")
        for subject in dict_of_students[student_first_last_name]:
            print(f"Subject '{subject}' - Grades {dict_of_students[student_first_last_name][subject]}")
        print_lines_logic_break()