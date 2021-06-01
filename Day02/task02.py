students = {}

num = int(input("How many students you want to enter: "))

for i in range(num):
    rollno = int(input("Enter roll-no: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    grade = None

    if marks > 90 and marks <=100:
        grade = "A"
    elif marks >80 and marks <=90:
        grade = "B"
    elif marks > 60 and marks <=80:
        grade = "C"
    elif marks >40 and marks <= 60:
        grade = "D"
    elif marks <=40 and marks>=0:
        grade = "Fail"
    else:
        grade = None
    
    key = "s" + str(i+1)
    student = {
        "No" : rollno,
        "Name": name,
        "Marks" : marks,
        "Grade" : grade
    }

    students[key] = student

print(students)