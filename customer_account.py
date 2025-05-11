
class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type="Savings", interest_rate=0.02, overdraft_limit=0.0):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.overdraft_limit = overdraft_limit
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
    
    def get_account_type(self):
        return self.account_type
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited £{amount:.2f} successfully.")
        else:
            print("Invalid deposit amount.")
        
    def withdraw(self, amount):
        #ToDo
        if amount <= 0:
           print("Invalid withdrawal amount.")
        elif amount > self.balance:
           print("Insufficient funds.")
        else:
           self.balance -= amount
           print(f"Withdrew £{amount:.2f} successfully.")
        pass
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def get_interest_payable(self):
      return self.balance * self.interest_rate if self.balance > 0 else 0.0

    def get_overdraft_taken(self):
      return abs(self.balance) if self.balance < 0 else 0.0
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        #STEP A.4.3
        print(f"Account No: {self.account_no}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Address: {', '.join(self.address)}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: £{self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100:.2f}%")
        print(f"Overdraft Limit: £{self.overdraft_limit:.2f}")

   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                try:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid input.")
                pass
            elif choice == 2:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input.")
                #ToDo
                pass
            elif choice == 3:
                #STEP A.4.4
                self.print_balance()
                pass
            elif choice == 4:
                #STEP A.4.2
                new_fname = input("Enter new first name: ")
                new_lname = input("Enter new last name: ")
                self.update_first_name(new_fname)
                self.update_last_name(new_lname)
                print("Name updated.")
                pass
            elif choice == 5:
                #ToDo
                new_address = input("Enter new address (comma-separated): ").split(",")
                self.update_address([a.strip() for a in new_address])
                print("Address updated.")
                pass
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")