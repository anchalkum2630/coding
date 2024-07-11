class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = None

    def set_pin(self, new_pin):
        if len(str(new_pin)) == 5:  
            self.pin = new_pin
            return "PIN set successfully."
        else:
            return "Invalid PIN."

    def check_balance(self, entered_pin):
        if self.pin == entered_pin:
            return self.balance
        else:
            return "Incorrect PIN."

    def deposit(self, amount, entered_pin):
        if self.pin == entered_pin:
            if amount > 0:
                self.balance=self.balance+amount
                return f"Deposited {amount}. New balance is {self.balance}."
            else:
                return "Invalid amount. Please enter a positive number."
        else:
            return "Incorrect PIN."

    def withdraw(self, amount, entered_pin):
        if self.pin == entered_pin:
            if amount > 0:
                if self.balance >= amount:
                    self.balance=self.balance- amount
                    return f"Withdrawn {amount}. New balance is {self.balance}."
                else:
                    return "Insufficient funds."
            else:
                return "Invalid amount. Please enter a positive number."
        else:
            return "Incorrect PIN."
atm = ATM(1000)
print(atm.set_pin(12345)) 
print(atm.check_balance(12345)) 
print(atm.deposit(500, 12345))  
print(atm.withdraw(200, 12345))  
print(atm.check_balance(99995))  
