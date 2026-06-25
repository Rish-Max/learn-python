

def student_report(students):
    marks = list(students.values())
    total_mark = sum(marks)
    average_mark = total_mark / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)
    return average_mark, highest_mark, lowest_mark

def view_students(students):
    students_list = list(students.items())
    if len(students_list) == 0:
        print("No students found.")
        return

    for student in students_list:
        print(f"Name: {student[0]}, Mark: {student[1]}")

def collect_students_details():
    students = {}
    while True:
        name = input("Enter the name of the student: ")
        already_exist_student = [name for student in students.keys() if student == name]
        
        if already_exist_student:
            print("Student already exist")
            continue
        
        mark = int(input("Enter the mark of the student: "))
        students[name] = mark
        
        isExit = input("Do you want to exit? (y/n): ") == "y"
        if isExit:
            break

    return students   

def main():
    students_list = collect_students_details()
    view_students(students_list)
    average_mark, highest_mark, lowest_mark = student_report(students_list)
    print(f"Average Marks : {average_mark:.2f}")
    print(f"Highest Marks : {highest_mark}")
    print(f"Lowest Marks : {lowest_mark}")
    print("Thank you for using the student mark analyzer.")

if __name__ == "__main__":
    main()