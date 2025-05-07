class Bank:
     bank_name = "AL Waqar Bank Limited" # Class variable

     def __init__(self, account_holder):
         self.account_holder = account_holder

     @classmethod
     def change_bank_name(cls, name): # Class Method
         cls.bank_name = name

     def display_info(self):  # Public Method
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank: {self.bank_name}")

# Creating instances
account1 = Bank("Waqar")
account2 = Bank("Waseem")

# Displaying initial bank name
print("Before changing bank name")
account1.display_info()
account2.display_info()

# Changing bank name using class method
Bank.change_bank_name("Al Waseem Bank Limited")

# Displaying updated bank name
print("After changing bank name")
account1.display_info()
account2.display_info()