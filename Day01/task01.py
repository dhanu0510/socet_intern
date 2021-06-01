lst = [1,2,3,['a','b','c'],4,5,6,['d','e','f'],7,'g',8,'h',[9,10,'i','j'],11, 
        "aansh",["priya"],[99,"softvan","nimesh",99],"hello"]



def print_list(lst):
    for i in lst:
        if type(i) == type(lst):
            print_list(i)
        else:
            if type(i) == type("a"):
                print("    " + str(i))
            else:
                print(i)

print_list(lst)