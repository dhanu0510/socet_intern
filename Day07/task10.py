from random import  randint
class BankInfo():
    def __init__(self,fn,ln,gender,address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address

class BankAccount(BankInfo):
    def __init__(self,ACno,amount,info):
        self.ACno = ACno
        self.amount = amount
        self.info = info



class Main():
    Info = []
    accounts = []
    types = []
    def __init__(self):
        fn = input("Enter FirstName:")
        ln = input("Enter LastName:")
        gender = input("Enter Gender:")
        address = input("Enter Address:")
        info = BankInfo(fn,ln,gender,address)

        ACno = randint(1000000000000,9999999999999)
        amount = int(input("Enter Amout:"))

        account = BankAccount(ACno,amount,info)
        TYPE = ""
        chance = 1
        while chance < 4:
            type = input("Enter type of account, saving or current:")
            if type == 'saving':
                if amount >=10000:
                    TYPE = "saving"
                    break
                else:
                    print("Choose Correct type according to your account details!")
                    chance += 1
            elif type == 'current':
                if amount >=5000:
                    TYPE = "current"
                    break
                else:
                    print("Choose Correct type according to your account details!")
                    chance += 1
            else:
                print("Choose Correct type according to your account details!")
        if chance >=4:
            exit(-1)
        else:
            self.accounts.append(account)
            self.Info.append(info)
            self.types.append(TYPE)
        
        month = int(input("Enter months:"))

        if self.types[-1] == 'current':
            print("No interest for current account")
        elif self.types[-1] == 'saving':
            current = amount
            for i in range(month):
                current = current + ((current*6)/100)
            print(f"Total Amount in you account after {month} month: {current}")

M = Main()
        

