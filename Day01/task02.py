students = {}

num = int(input("Enter no of students:"))

for i in range(num):
	print("STUDENT " + str(i+1))
	name = input("Enter name: ")
	no = int(input("Enter no: "))
	marks = float(input("Enter marks:"))
	student = [name,marks]
	students[no] = student

print(students)    
num = int(input("Enter num:"))
print(student[num])
