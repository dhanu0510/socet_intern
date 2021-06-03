file_name = "demo.txt"

lines = int(input("How many lines you want to enter:"))

def input_data(i):
    data = input("Ener data for line"+str(i) + ":")
    data = data + "\n"
    fo = open(file_name, "a+")
    fo.write(data)
    fo.close()

for i in range(lines):
    input_data(i+1)

fo = open(file_name,"r")
data = fo.read()

lst = []

lst_demo = ""
for word in data:
    if word =='\n':
        lst.append(lst_demo)
        lst_demo = ""
    else:
        lst_demo = lst_demo + word
fo.close()

# print(lst)
x = input("Which word you want to replace:")
y = input("with what word?:")

new_lst = []
for line in lst:
    line = line.replace(x,y)
    new_lst.append(line)

new_lst.reverse()
# print(new_lst)

for line in new_lst:
    data = line + "\n"
    fo = open("dummy.txt", "a+")
    fo.write(data)
    fo.close()
