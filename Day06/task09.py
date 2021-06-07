class StudentInfo():
    def __init__(self,name,no):
        self.name = name
        self.no = no

class StudentMarks():
    MARKS = []
    def __init__(self,no,m1,m2,m3):
        mark = []
        mark.append(m1)
        mark.append(m2)
        mark.append(m3)
        self.MARKS.append(mark)

class main():
    INFO = []
    MARKS = []
    NAME = []
    NO = []
    def __init__(self):
        self.n = int(input("Enter no of students: "))
    
    def input_studentInfo(self):
        name = input("Enter name: ")
        no = int(input("Enter no:"))
        info = StudentInfo(name,no)
        self.NAME.append(name)
        self.NO.append(no)
        self.INFO.append(info)
    def input_studentMarks(self):
        m1 = int(input("Enter marks1:"))
        m2 = int(input("Enter marks2:"))
        m3 = int(input("Enter marks3:"))
        marks = StudentMarks(no,m1,m2,m3)
        self.MARKS.append(marks)

s = main()
for i in range(s.n):
    s.input_studentInfo()
    s.input_studentMarks()

for i in range(s.n):
    print("Student name:",s.NAME[i])
    print(s.NAME[i],":",s.NO[i])
    print(s.NAME[i],"marks:",s.MARKS[i].MARKS[i])