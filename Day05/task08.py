n = int(input("How many students?:"))

roll_no = []
name = []
marks = []
average = []
grade = []
def take_input():
    temp_name = input("Enter name:")
    temp_no = input("Enter no:")
    temp_marks = []
    sum = 0
    for i in range(3):
        temp_temp_marks = int(input("Enter marks for subject " + str(i+1) + ":"))
        temp_marks.append(temp_temp_marks)
        sum = sum + temp_temp_marks
    marks.append(temp_marks)
    roll_no.append(temp_no)
    name.append(temp_name)
    avg = sum /3
    average.append(avg)
    if avg >=80 and avg <=100:
        grade.append("A")
    elif avg >=60 and avg<80:
        grade.append("B")
    elif avg >=40 and avg < 60:
        grade.append("C")
    elif avg <40 and avg >=0:
        grade.append("D")
    else:
        grade.append("Error")
def studentInfo(no,name):
    data = no + "-" + name + "\n"
    fo = open("studentInfo.txt", "a+")
    fo.write(data)
    fo.close()
def studentMarks(no,marks):
    data = no
    for i in marks:
        data = data + "-" + str(i)
    data = data + "\n"
    fo = open("studentMarks.txt", "a+")
    fo.write(data)
    fo.close()
def avg(no,grade,avg):
    data = str(no) + "-" + str(grade) + "-" + str(avg) + "\n"
    file_name = grade + ".txt"
    fo = open(file_name, "a+")
    fo.write(data)
    fo.close()



for i in range(n):
    take_input()

for i in range(n):
    studentInfo(roll_no[i],name[i])
    studentMarks(roll_no[i],marks[i])
    avg(roll_no[i],grade[i],average[i])
