#bank account system

class BankAccount:
	def __init__(self, account_number: str, account_holder: str, password: str):
		self.account_number = account_number
		self.account_holder = account_holder
		self.password = password
		self.balance = 0.0

	def deposit(self, amount: float):
		self.balance += amount

	def withdraw(self, amount: float):
		if self.balance - amount < 0:
			return -1
		self.balance -= amount
		return self.balance

	def display_balance(self):
		return self.balance

	def check_login(self, user, password):
		if self.account_holder == user and self.password == password:
			return True
		return False


accounts = list()

while True:
	print("\n---------------------------------------------")
	print("What do you wish to do..?")
	print("1. Create acount")
	print("2. Login")
	print("3. Exit")
	choice = int(input("Enter choice: "))
	
	if choice == 1:
		name = input("\nEnter Name: ")
		password = input("Enter password: ")
		account_number = len(accounts)+1
		accounts.append(BankAccount(account_number, name, password))
		print("\n---ACCOUNT CREATED---")
	elif choice == 2:
		user = input("\nEnter username: ")
		password = input("Enter password: ")
		flag = 1
		for i in accounts:
			if i.check_login(user, password):
				flag = 0
				while True:
					print("\n-----------------------------------------------")
					print("What do you wish to do..?")
					print("1. Deposit amount")
					print("2. Withdraw amount")
					print("3. Check balance")
					print("4. Log Out")
					choice2 = int(input("Enter choice: "))

					if choice2 == 1:
						amount = float(input("\nEnter the amount: "))
						i.deposit(amount)
					elif choice2 == 2:
						amount = float(input("Enter the amount: "))
						if i.withdraw(amount) == -1:
							print("\n---INSUFFECIENT FUNDS---")
						else:
							print("\n---AMOUNT WITHDRAWN---")
					elif choice2 == 3:
						print("\nCurrent balance: ", i.display_balance())
					elif choice2 == 4:
						print("\n***YOU HAVE BEEN LOGGEDOUT***")
						break
					else:
						print("\n---INVALID INPUT---")
		if flag:
			print("\n---ACCOUNT NOT FOUND---")
	elif choice == 3:
		print("***YOU HAVE EXITED THE PROGRAM***")
		break
	else:
		print("---INVALID INPUT---")
		
