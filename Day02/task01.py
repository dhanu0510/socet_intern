x = input().split(',')
str_list = []
int_list = []

for i in x:
    try:
        int_list.append(int(i))
    except:
        str_list.append(i)

print("Max:",max(int_list))
print("Min:",min(int_list))
print(int_list)


str_list.reverse()
print(str_list)