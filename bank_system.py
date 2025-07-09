import json
from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
	if not self.admins_list:
          self.load_default_customers()
    
    def load_bank_data(self, filename="bank_data.json"):
        filename = filename 
        if not filename.endswith(".json"):
            filename += ".json"

        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.accounts_list = []
            for c in data.get("customers", []):
                customer = CustomerAccount(
                    c["fname"], c["lname"], c["address"],
                    c["account_no"], c["balance"],
                    c["account_type"], c["interest_rate"], c["overdraft_limit"]
                )
                self.accounts_list.append(customer)

            self.admins_list = []
            for a in data.get("admins", []):
                admin = Admin(
                    a["fname"], a["lname"], a["address"],
                    a["user_name"], a["password"], a["full_rights"]
                )
                self.admins_list.append(admin)

            print(f"Data loaded from '{filename}'.")

        except FileNotFoundError:
            print("File not found. Using default data.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")
        except Exception as e:
            print("Error loading data:", e)
            
        
        # create customers
    def load_default_customers(self):
            
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00,  "Current", 0.01, 1000.00)
        self.accounts_list.append(customer_1)
        
        account_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00, "Savings", 0.03, 0.00)    
        self.accounts_list.append(customer_2)

        account_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00, "Premium Savings", 0.05, 500.00)
        self.accounts_list.append(customer_3)

        account_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00, "Basic", 0.01, 0.00)
        self.accounts_list.append(customer_4)
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)


    def search_admins_by_name(self, admin_username):
        #STEP A.2
      for admin in self.admins_list:
        if admin.get_username() == admin_username:
            return admin
            return None
              
        
    def search_customers_by_name(self, customer_lname):
        #STEP A.3
        for customer in self.accounts_list:
         if customer.get_last_name().lower() == customer_lname.lower():
           return customer
           return None
        pass

    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        try:
         option = int(input("Choose your option: "))
         if option == 1 or option == 2:
           return option
         else:
           print("Invalid option. Please choose 1 or 2.")
        except ValueError:
         print("Invalid input. Please enter a number.")


    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        #ToDo
            sender = self.search_customers_by_name(sender_lname)
            receiver = self.search_customers_by_name(receiver_lname)
            
            if not sender or not receiver:
                print("Sender or receiver not found.")
                return
            if str(receiver.get_account_no()) != str(receiver_account_no):
                print("Receiver account number mismatch.")
                return

            elif sender.get_balance() < amount:
                  print("Insufficient funds.")
                  return
            else:
                  sender.withdraw(amount)
                  receiver.deposit(amount)
                  print("Transfer successful.")
                  
                  
    
    def save_to_file(self):
        filename = input("Enter filename to save (e.g., data.json): ").strip()
        if not filename.endswith(".json"):
            filename += ".json"

        data = {
            "customers": [{
                "fname": c.get_first_name(),
                "lname": c.get_last_name(),
                "address": c.get_address(),
                "account_no": c.get_account_no(),
                "balance": c.get_balance(),
                "account_type": c.account_type,
                "interest_rate": c.interest_rate,
                "overdraft_limit": c.overdraft_limit
            } for c in self.accounts_list],
            
            "admins": [{
                "fname": a.get_first_name(),
                "lname": a.get_last_name(),
                "address": a.get_address(),
                "user_name": a.get_username(),
                "password": a.get_password(),
                "full_rights": a.has_full_admin_right()
            } for a in self.admins_list]
        }

        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to '{filename}'.")
        except Exception as e:
            print("Error saving data:", e)

                
    def admin_login(self, username, password):
		  #STEP A.1
          admin = self.search_admins_by_name(username)
          if admin:
           if admin.get_password() == password:
               return "Login successful.", admin
           else:
               print(password)
               return "Incorrect password.", None
          else:
              return "Admin not found.", None
              pass

    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Update Admin Information")
         print("6) Add new customer")
         print("7) Management Report")
         print("9) Save data to JSON file")
         print("10) Load data from JSON file")
         print("11) Sign out")
         print (" ")
         try:
           option = int(input("Choose your option: "))
           if option in range(1, 11+1):
               print()
               return option
           else:
               print("Invalid option. Please choose from 1 to 11.")
         except ValueError:
           print("Invalid input. Please enter a number.")

    def create_new_customer(self):
         print("\n--- Create New Customer ---")
         fname = input("Enter first name: ")
         lname = input("Enter last name: ")
         address = input("Enter address (comma-separated): ").split(",")
         address = [a.strip() for a in address]
         account_no = max([c.get_account_no() for c in self.accounts_list], default=1234) + 1

         print("Choose account type:")
         print("1) Savings (2%, £0 overdraft)")
         print("2) Current (1%, £500 overdraft)")
         print("3) Premium Savings (3%, £0 overdraft)")
         acc_type_choice = input("Choice: ")
         if acc_type_choice == "2":
              acc_type, rate, overdraft = "Current", 0.01, 500.0
         elif acc_type_choice == "3":
              acc_type, rate, overdraft = "Premium Savings", 0.03, 0.0
         else:
              acc_type, rate, overdraft = "Savings", 0.02, 0.0
         try:
             balance = float(input("Initial balance: "))
             if balance < 0:
              raise ValueError("Initial balance cannot be negative.")
         except ValueError as ve:
                print("Error:", ve)
                return
         customer = CustomerAccount(fname, lname, address, account_no, balance, acc_type, rate, overdraft)
         self.accounts_list.append(customer)
         print("Customer created successfully.")

    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)                    
            elif choice == 2:
                #STEP A.4
                lname = input("\n Please input customer's last name: ")
                customer = self.search_customers_by_name(lname)
                if customer:
                 customer.run_account_options()
                else:
                 print("Customer not found.")
                 
            
            elif choice == 3:
                #Todo
                lname = input("\n Please input customer's last name to delete: ")
                customer = self.search_customers_by_name(lname)
                if customer in self.accounts_list:
                    self.accounts_list.remove(customer)
                    print("Customer deleted.")
                   
           

            elif choice == 4:
            #Todo
                self.print_all_accounts_details()
                
            elif choice == 5:
                # Update admin info
                print("\n--- Update Admin Information ---")
                new_fname = input("Enter new first name: ")
                new_lname = input("Enter new last name: ")
                new_address = input("Enter new address (comma-separated): ").split(",")
                new_address = [part.strip() for part in new_address]

                admin_obj.update_first_name(new_fname)
                admin_obj.update_last_name(new_lname)
                admin_obj.update_address(new_address)

                print("Admin information updated successfully.")
                
            elif choice == 6:
                self.create_new_customer()
                
            elif choice == 7:
                self.print_management_report()
                
            elif choice == 9:
               self.save_to_file()
            elif choice == 10:
                self.load_bank_data()
                print("Data loaded successfully from file.")
            
            elif choice ==11:
                loop = 0
                print ("\n Exit account operations")
                
    def print_management_report(self):
        total_customers = len(self.accounts_list)
        total_balance = sum(acc.get_balance() for acc in self.accounts_list)
        total_interest = sum(acc.get_interest_payable() for acc in self.accounts_list)
        total_overdraft = sum(acc.get_overdraft_taken() for acc in self.accounts_list)

        print("\n--- Management Report ---")
        print(f"Total customers: {total_customers}")
        print(f"Total balance across accounts: £{total_balance:.2f}")
        print(f"Total interest (1 year): £{total_interest:.2f}")
        print(f"Total overdraft taken: £{total_overdraft:.2f}")


    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("---------")

if __name__ == "__main__":
    app = BankSystem()
app.run_main_options()
