class Bank():
    ac_num:int
    name:str
    ac_type:str
    ifsc_code:int
    branch:str
    balance:int

    def create_ac(self,ac_num,name,ac_type,ifsc_code,branch,balance):
        self.ac_num=ac_num
        self.name=name
        self.ac_type=ac_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.ac_num} has been credited with {amount} available balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"your {self.ac_num} has been credited with {amount} available balance is {self.balance}")

    def get_balance(self):
        print(f"available balance is {self.balance}")

bank1=Bank()
bank1.create_ac(1002,"anu","sb",1000200,"calicut",0)
bank1.deposit(1000)
bank1.get_balance()
bank1.withdraw(500)
bank1.get_balance()

bank2=Bank()
bank2.create_ac(1002,"anu","sb",1000200,"calicut",1000)
bank2.deposit(4000)
bank2.get_balance()
bank2.withdraw(600)
bank2.get_balance()



