class BankAccount:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        print("Amount withdrawn successfully.")

    def display_details(self):
        print("\nAccount Number :", self.account_number)
        print("Customer Name  :", self.name)
        print("Balance        :", self.balance)

    def calculate_interest(self, rate):
        if rate <= 0:
            raise ValueError("Interest rate must be greater than 0")

        interest = self.balance * rate / 100
        return interest


class SavingsAccount(BankAccount):

    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)


class CurrentAccount(BankAccount):

    def __init__(self, account_number, name, balance, overdraft_limit):
        super().__init__(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")

        maximum_withdrawal = self.balance + self.overdraft_limit

        if amount > maximum_withdrawal:
            raise ValueError("Withdrawal exceeds overdraft limit")

        self.balance -= amount
        print("Amount withdrawn successfully.")

    def display_details(self):
        super().display_details()
        print("Overdraft Limit:", self.overdraft_limit)


accounts = {}


def create_account():

    try:
        account_number = int(input("Enter account number: "))

        if account_number in accounts:
            print("Account number already exists.")
            return

        name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        print("\n1. Savings Account")
        print("2. Current Account")

        account_type = input("Enter account type: ")

        if account_type == "1":

            account = SavingsAccount(
                account_number,
                name,
                balance
            )

        elif account_type == "2":

            overdraft_limit = float(
                input("Enter overdraft limit: ")
            )

            if overdraft_limit < 0:
                raise ValueError("Overdraft limit cannot be negative")

            account = CurrentAccount(
                account_number,
                name,
                balance,
                overdraft_limit
            )

        else:
            raise ValueError("Invalid account type")

        accounts[account_number] = account

        print("Account created successfully.")

    except ValueError as e:
        print("Error:", e)


def deposit_money():

    try:
        account_number = int(
            input("Enter account number: ")
        )

        if account_number not in accounts:
            raise ValueError("Invalid account number")

        amount = float(
            input("Enter deposit amount: ")
        )

        account = accounts[account_number]

        account.deposit(amount)

        print("Current Balance:", account.balance)

    except ValueError as e:
        print("Error:", e)


def withdraw_money():

    try:
        account_number = int(
            input("Enter account number: ")
        )

        if account_number not in accounts:
            raise ValueError("Invalid account number")

        amount = float(
            input("Enter withdrawal amount: ")
        )

        account = accounts[account_number]

        account.withdraw(amount)

        print("Current Balance:", account.balance)

    except ValueError as e:
        print("Error:", e)


def view_account():

    try:
        account_number = int(
            input("Enter account number: ")
        )

        if account_number not in accounts:
            raise ValueError("Invalid account number")

        account = accounts[account_number]

        account.display_details()

    except ValueError as e:
        print("Error:", e)


def calculate_interest():

    try:
        account_number = int(
            input("Enter account number: ")
        )

        if account_number not in accounts:
            raise ValueError("Invalid account number")

        rate = float(
            input("Enter interest rate (%): ")
        )

        account = accounts[account_number]

        interest = account.calculate_interest(rate)

        print("Interest:", interest)

    except ValueError as e:
        print("Error:", e)


while True:

    print("\n================================")
    print("       MINI BANKING SYSTEM")
    print("================================")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account Details")
    print("5. Calculate Interest")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        view_account()

    elif choice == "5":
        calculate_interest()

    elif choice == "6":
        print("Thank you for using the banking system.")
        break

    else:
        print("Invalid menu choice. Please try again.")
        
        
# ================================
#        MINI BANKING SYSTEM
# ================================
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. View Account Details
# 5. Calculate Interest
# 6. Exit
# Enter your choice: 1

# Enter account number: 101
# Enter customer name: Rahul
# Enter initial balance: 10000

# 1. Savings Account
# 2. Current Account
# Enter account type: 1

# Account created successfully.


# ================================
#        MINI BANKING SYSTEM
# ================================
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. View Account Details
# 5. Calculate Interest
# 6. Exit
# Enter your choice: 4

# Enter account number: 101

# Account Number : 101
# Customer Name  : Rahul
# Balance        : 10000.0


# ================================
#        MINI BANKING SYSTEM
# ================================
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. View Account Details
# 5. Calculate Interest
# 6. Exit
# Enter your choice: 2

# Enter account number: 101
# Enter deposit amount: 5000
# Amount deposited successfully.
# Current Balance: 15000.0


# ================================
#        MINI BANKING SYSTEM
# ================================
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. View Account Details
# 5. Calculate Interest
# 6. Exit
# Enter your choice: 3

# Enter account number: 101
# Enter withdrawal amount: 3000
# Amount withdrawn successfully.
# Current Balance: 12000.0


# ================================
#        MINI BANKING SYSTEM
# ================================
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. View Account Details
# 5. Calculate Interest
# 6. Exit
# Enter your choice: 5

# Enter account number: 101
# Enter interest rate (%): 5
# Interest: 600.0


# ================================
#        MINI BANKING SYSTEM
# ================================
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. View Account Details
# 5. Calculate Interest
# 6. Exit
# Enter your choice: 6

# Thank you for using the banking system.