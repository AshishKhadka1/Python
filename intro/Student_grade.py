# Nested dictionary to store students and their subjects

students = {}

def add_student():
    name = input("Enter Student name: ")
    subjects = int(input("How Many Subjects ?"))
    
    students[name] = {}

    for i in range(subjects):
        subject = input("Enter subject name :")
        grade = float(input("Enter grade for {subject}: "))
        students[name][subject] = grade
    
print("Student Added successfully")

def update_grade():
    name = input("Enter student name: ")
    
    if name in students:
        subject = input ("Enter subject name: ")
    
        if subject in students[name]:
            grade = float(input("Enter new grade: "))
            students[name][subject] = grade
            print("Grade updated successfully. ")
        else:   
            print("Subject not found")
    else:
        print("Student not found. ")
        
def calculate_average():
    name = input ("Enter student name: ")
    
    if name in students:
        grades = students[name].values()
        average = sum(grades) / len(grades)
        print(f"Average grade of {name} is : {average}")
    else:
        print("Student not found.")
        
while True:
    print("\n1. Add Stundet")
    print("2. Update Student Grade")
    print("3. Calculate Average Grade")
    print("4. Exit")
    
    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice =="3":
        calculate_average()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
    
    
        
        