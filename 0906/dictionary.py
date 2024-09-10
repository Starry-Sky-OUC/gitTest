students = {}

def add_student(student_id, name):
    if student_id in students:
        print(f"{student_id} exist")
    else:
        students[student_id] = name
        print("success")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print("success")
    else:
        print(f"{student_id} not found")

def update_student(student_id, name):
    if student_id in students:
        students[student_id] = name
        print("success")
    else:
        print(f"{student_id} not found")

def get_student(student_id):
    if student_id in students:
        print(f"{student_id}: {students[student_id]}")
    else:
        print(f"{student_id} not found")

def display_all_students():
    if students:
        print("All students:")
        for student_id, name in students.items():
            print(f"{student_id}: {name}")
    else:
        print("None")

add_student("202401", "Tom")
add_student("202402", "Jerry")
display_all_students()

update_student("202401", "Bob")
get_student("202401")

delete_student("202402")
display_all_students()