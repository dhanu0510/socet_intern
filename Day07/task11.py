
sign_up = False
sign_in = False

# // ASCII : a-z=97-122  ,A-Z=65-90, 0-9:48-57

class SignUp():
    def __init__(self,fn,ln,un):
        pw = input(("Enter Password:"))

        try:
            l = len(pw)
            lower = False
            upper = False
            number = False
            symbols = False
            for i in pw:
                ascii = ord(i)
                if ascii >=97 and ascii <=122:
                    lower = True
                elif ascii >=65 and ascii <= 90:
                    upper = True
                elif ascii >=48 and ascii <= 57:
                    number = True
                else:
                    symbols = True
            if l>=8 and l<=16 and lower and upper and number and symbols:
                self.pw = pw
                global sign_up
                sign_up = True
            else:
                error = int("Error")                
            
        except:
            print("You must fullfil the condition.")

class SignIn():
    def __init__(self,user,pas):
        u = input("Enter Username:")
        p = input("Enter Password:")

        if user == u and pas == p:
            print("Welcome, you have successfully logged in!")
            global sign_in
            sign_in = True
        else:
            print("You entered wrong details!")



fn = input("First Name:")
ln = input("Last Name:")
un = input("Enter Username:")

while not sign_up:
    s = SignUp(fn,ln,un)
while not sign_in:
    signin = SignIn(un,s.pw)










