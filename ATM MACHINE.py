### ATM MACHINE ###
user = ("leo")
password = "123"
bank_balance = 1000
# Ask the client to enter his credentials to access his account
access = input("please enter your username: ")
if access == user:
    access_1 = input("please enter your password: ")
    if access_1 == password:
        print("")
        print("Welcome to your account", user)
    else:
        print ("your password it's incorrect")
else: 
    print ("user not found!")

# A menu option displays, containing all the actions the user can make
# the "while" will allow me to repeat the code if the user decides to display the menu again
while True:
    if access_1 == password: 
        print ("")
        print ("¿Which operation would you like to make?")
        print ("")
        print ("1.CHECK CURRENT BALANCE --- 2.WITHDRAW YOUR MONEY --- 3.DEPOSIT MONEY")
        operation = input("Please enter the number of the operation you would like to make: ")
        if operation == "1":
            print("Your current balance is ${}" .format(bank_balance))
        elif operation == "2":
            take = int(input("How much would you like to withdraw?: "))
            if take <= bank_balance:
                print ("You withdrawed ${} and Your current balance is ${}" .format(take, (bank_balance - take)))
                # we do this to update the value of the balance, specifically the assigned variable for the value of the client's balance
                bank_balance = bank_balance - take 
            else:
                print("Insuficient fonds, please select another amount")
        elif operation == "3":
            add = int(input("How much would you like to deposit?: "))
            print("You deposited ${} and Your current balance is ${}" .format(add, (bank_balance + add)))
            # we do this to update the value of the balance, specifically the assigned variable for the value of the client's balance
            bank_balance = bank_balance + add
        else:
            print("¡PLEASE CHOOSE A VALID OPTION!")
        # we verify if the client wish to display the menu again
        check = input ("1.Do you want to exit or 2.Do you want to go back to the main menu: ")
        if check == "2":
            continue
        else:
            print("Thanks for using Leo's ATM!")
            break