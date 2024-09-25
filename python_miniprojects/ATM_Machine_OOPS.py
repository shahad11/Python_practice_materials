

class AtmMachine:

    def __init__(self):
        self.balance = 0
        self.pin = ""
        self.main()
    

    def main(self):
        result = int(input("Press 1 if new user to set password\
                           Press 2 to deposite amount\
                           Press 3 to know balance\
                           press 4 to withdraw amount\
                           Input here and press enter: "))
        
        if result ==1:
            #Set password
            self.set_pin()
            

        if result == 2:
            #Deposit amount
            self.deposit()

        if result == 3:
            # Balance
            self.currentbalance()

        if result == 4:
            #Withdraw
            self.withdraw()

        else:
            exit()
        
    def set_pin(self):
        new_pin = input("Input your new pin here: ")
        self.pin = new_pin
        self.main()

    def deposit(self):
        pin_check = input("Input your pin: ")
        if pin_check == self.pin:
            new_deposit = int(input("Enter how much cash to top up:"))
            self.balance += new_deposit
            print(f"your new balance is {self.balance}")
            self.main()
        else:
            print("invalid pin")
            self.main()
    def currentbalance(self):
        pin_check = input("Input your pin: ")
        if pin_check == self.pin:
            print(f"Your current balance is {self.balance}")
            self.main()
        else:
            print("Invalid Pin")
            self.main()

    def withdraw(self):
        pin_check = input("Input your pin: ")
        if pin_check == self.pin:
            withdraw_amount = int(input("Input withdraw amount: "))
            if withdraw_amount > self.balance:
                print("Inusufficiant Balance")
                self.main()
            else:
                self.balance -= withdraw_amount
                print(f"Your current balance is {self.balance}")
                self.main()
        else:
            print("Invalid Pin")
            self.main()       

        

atm = AtmMachine()
