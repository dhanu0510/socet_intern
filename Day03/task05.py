num = int(input("How many list:"))
lsts = []
for i in range(num):
  lst = input("Enter num for list "+str(i+1)+":").split(',')
  lsts.append(lst)
def fun1(lst):
  print(lst)
def fun2(lst1,lst2):
  new_list = lst1+lst2
  print("max:",max(new_list))
  print("min:",min(new_list))
def fun3(lst1,lst2,lst3):
  new_list = lst1+lst2+lst3
  sum = 0
  for j in new_list:
    sum = sum + int(j)
  print("sum:",sum)
def fun4(lst):
  new_list = []
  for j in lst:
    new_list = new_list + j
  odd_list = []
  for j in new_list:
    if int(j)%2==1:
      odd_list.append(j)
    print(int(j)*int(j))
  print("Odd numers:")
  print(odd_list)
if num==1:
  fun1(lsts[0])
elif num==2:
  fun2(lsts[0],lsts[1])
elif num==3:
  fun3(lsts[0],lsts[1],lsts[2])  
else:
  fun4(lsts)