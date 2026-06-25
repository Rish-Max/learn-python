

def average_mark(students_list):
    total_mark = 0
    highest_mark= None
    lowest_mark = None

    for students in students_list:
        student_mark = int(students["mark"])
        if lowest_mark == None or student_mark < lowest_mark:
            lowest_mark = student_mark
        if highest_mark == None or student_mark > highest_mark:
            highest_mark = student_mark
        total_mark += student_mark

    print(f"""
    Average Marks : {total_mark / len(students_list):.2f}
    Highest Marks : {highest_mark}
    Lowest Marks : {lowest_mark}
    """)

    return total_mark / len(students_list) ,highest_mark,lowest_mark

def view_students(students_list):
    if len(students_list) == 0:
        print("No students found.")
        return

    for student in students_list:
        print(f"Name: {student['name']}, Mark: {student['mark']}")

def add_students():
    students_list = []
    while True:
        name = input("Enter the name of the student: ")
        mark = input("Enter the mark of the student: ")

        isStudentExists = False
        for student in students_list:
            if student["name"] == name:
                print("Student already exists.")
                isStudentExists = True
                break

        if not isStudentExists:
            students_list.append({"name": name, "mark": mark})
        
        isExit = input("Do you want to exit? (y/n): ") == "y"
        if isExit:
            break

    return students_list    

def main():
    students_list = add_students()
    view_students(students_list)
    average_mark(students_list)

main()