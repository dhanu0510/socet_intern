class HDFCBANK():

    def __init__(self):
        self.limit = 3
        self.amount = 20000
    
    def transaction(self,amount):
        self.amount -= amount
        self.limit -= 1

class AXISBANK():
    def __init__(self):
        self.limit = 5
        self.amount = 30000
    
    def transaction(self,amount):
        self.amount -= amount
        self.limit -= 1

class ATM():
    def __init__(self):
        run = True
        bank_type = input("Which bank do you wanna select? AXIS or HDFC :  ")
        if bank_type == "AXIS":
            bank = AXISBANK()
        elif bank_type == "HDFC":
            bank = HDFCBANK()
        else:
            exit(-1)
        
        while run:
            amount = int(input("Enter Amount:"))
            if bank.amount >= amount:
                if bank.limit > 0:
                    bank.transaction(amount)
                    print("Transaction successful!")
                else:
                    print("Transactoin limit over!")
                    exit(-1)
                    
            else:
                print("Not enough amount!")

            nxt = input("Do you wanna withdrawl more money? YES/NO:")
            if nxt == "NO":
                run = False

atm = ATM()