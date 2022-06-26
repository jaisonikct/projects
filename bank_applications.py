import os
from getpass import getpass
print("=====================================")

customerNames = ['jai soni', 'sachin yadav', 'saurabh jain']
customerPins = ['0123', '0123', '0123']
customerBalances = [10000, 20000, 20000]
deposition = 0
withdrawal = 0
balance = 0
while True:
    os.system("cls")
    print("=====================================")
    print(" ----Welcome to the bank of python----       ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Login                      >>=")
    print("=<< 3. Exit/Quit                  >>=")
    print("*************************************")
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        name = input("Input Fullname : ")
        customerNames.append(name)
        pin = getpass("Please input a pin of your choice : ")
        customerPins.append(pin)
        balance = 0
        deposition = eval(input("Please input a value to deposit to start an account : "))
        balance = balance + deposition
        customerBalances.append(balance)
        print("\nYour name is added to customers system")
        print("Your pin is added to customer system")
        print("Your balance is added to customer system")
        print("----New account created successfully !----")
        print("\n")
        print("\n")
        print("Note! Please remember the Name and Pin")
        print("========================================")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = getpass("Please input pin : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("*************************************")
                        print("=<< 1. Withdraw money         >>=")
                        print("=<< 2. Deposit money          >>=")
                        print("=<< 3. Check balance          >>=")
                        print("=<< 4. Exit/Quit              >>=")
                        print("*************************************")
                        ch = int(input("Select your choice number from the above menu : "))    
                        if ch == 1:
                                print("Your Current Balance:", end=" ")
                                print(customerBalances[k], end=" ")
                                print("-/Rs\n")
                                balance = (customerBalances[k])
                                withdrawal = eval(input("Input value to Withdraw : "))
                                if withdrawal > balance:
                                    deposition = eval(input("Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                                    balance = balance + deposition
                                    print("Your Current Balance:", end=" ")
                                    print(balance, end=" ")
                                    print("-/Rs\n")
                                    balance = balance - withdrawal
                                    print("-\n")
                                    print("----Withdraw Successfull!----")
                                    customerBalances[k] = balance
                                    print("Your New Balance: ", balance, end=" ")
                                    print("-/Rs\n\n")
                                else:
                                    balance = balance - withdrawal
                                    print("\n")
                                    print("----Withdraw Successfull!----")
                                    customerBalances[k] = balance
                                    print("Your New Balance: ", balance, end=" ")
                                    print("-/Rs\n\n")
            if j < 1:
                print("Your name or pin does not match! Please Enter correct Details\n")
                break
            elif ch == 2:
                            deposition = eval(input("Enter the value you want to deposit : "))
                            balance = balance + deposition
                            customerBalances[k] = balance
                            print("\n")
                            print("----Deposition successful!----")
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            elif ch ==3:
                print(f"Hello {name} Your Current Balance is:", end=" ")
                print(customerBalances[k], end=" ")
                print("-/Rs\n")
                balance = (customerBalances[k]) 
            elif ch == 4:
                print("Thank you for using our banking system!")
                print("\n")
                print("We Hope to see you again:)")
                print("Bye bye")
                break
    elif choiceNumber == "3":
        print("Thank you for using our banking system!")
        print("\n")
        print("We Hope to see you again:)")
        print("Bye bye")
        break
    else:
        print("Invalid option selected by the customer")
        print("Please Try again!")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
