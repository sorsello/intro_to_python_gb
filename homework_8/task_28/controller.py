from common.console_helpers import capture_user_input_number
from homework_7.task_27.console_command_service import exit_program
from homework_8.task_28.grading_service import add_grade_to_student_one_subject, display_all_grades_for_student
from homework_8.task_28.school_subject_service import add_subject_to_all_students
from homework_8.task_28.student_service import add_student, display_all_students_first_last_name

def run_the_application(action_number:int, dict_of_students) -> None:
    if action_number == 1:
        print("---- Adding a new student ----")
        student_first_name: str = input("Please enter a student First Name: ")
        student_last_name: str = input("Please enter a student Last Name: ")
        add_student(dict_of_students, student_first_name, student_last_name)
    elif action_number == 2:
        print("---- Adding a subject to all students ----")
        subject_to_add: str = input("Please enter a subject to add to all students: ")
        add_subject_to_all_students(dict_of_students, subject_to_add)
    elif action_number == 3:
        print("---- Adding a subject grade to a student ----")
        student_first_name: str = input("Please enter a student First Name: ")
        student_last_name: str = input("Please enter a student Last Name: ")
        target_subject: str = input("Please enter a subject to add a grade to: ")
        grade_to_add: int = capture_user_input_number("Please enter a grade to add: ")
        add_grade_to_student_one_subject(dict_of_students, student_first_name, student_last_name, target_subject, grade_to_add)
    elif action_number == 4:
        print("---- Showing all students ----")
        display_all_students_first_last_name(dict_of_students)
    elif action_number == 5:
        print("---- Showing all grades for a student ----")
        student_first_name: str = input("Please enter a student First Name: ")
        student_last_name: str = input("Please enter a student Last Name: ")
        display_all_grades_for_student(dict_of_students, student_first_name, student_last_name)
    elif action_number == 6:
        print("---- Exiting the program ----")
        exit_program()