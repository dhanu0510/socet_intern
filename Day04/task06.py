file_name = input("Enter file name:")
file_name = file_name + ".txt"

lines = int(input("How many lines you want to enter:"))

def input_data(i):
    data = input("Ener data for line"+str(i) + ":")
    data = data + "\n"
    fo = open(file_name, "a+")
    fo.write(data)
    fo.close()

for i in range(lines):
    input_data(i+1)

file = open(file_name, "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
data = file.read()
words = data.split()

file.close()
print('Number of words in text file :', len(words))
print("No of lines:",line_count)