import logging
import sys

opt = 0

cust_profile = open("cust_profile.txt", "a+")

def end():
    print('SESSION TERMINATED!!!')
    print('------------------')
    print('******************')
    print('THANK YOU FOR VISITING!!!')
    print('******************')
    print('------------------')
    print('------------------')
    print('******************')
    print('HAVE A NICE DAY!!!')
    print('******************')
    print('------------------')
    sys.exit()

def transact():
    username = input('Please enter username:')
    transactionfilename = username + '_transactionhistory.log'
    with open(transactionfilename, 'r') as f:
        f.seek(0)
        if f.read(1):
            print(f.read())
        else:
            print('There is no transaction history.')
        opt()

def depositcash():
    deposit_amount = float(input('Please enter amount to be deposited:'))
    username = input('Please enter username:')
    filename = username + '.txt'
    transactionfilename = username + '_transactionhistory.log'
    file = open(filename, 'a')
    balance = 0
    new_balance = 0
    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open(filename, 'w+') as file2:
        new_balance = balance + deposit_amount
        new_balance = str(new_balance)
        file2.write(new_balance)
        print('Your new balance is:', new_balance)
    with open(transactionfilename, 'a') as file3:
        balance = str(balance)
        deposit_amount = str(deposit_amount)
        logging.basicConfig(filename = transactionfilename, level = logging.INFO, format ='%(asctime)s %(message)s')
        logging.warning('is when this event was logged.')
        file3.write('Previous balance: ' + balance + '. Deposit amount is:' + deposit_amount + '. New balance:' + new_balance + '\n')
    file.close()
    opt()

def withdrawalcash():
    withdrawn_amount = float(input('Please enter amount to be withdrawn:'))
    username = input('Please enter username:')
    filename = username + '.txt'
    transactionfilename = username + '_transactionhistory.log'
    file = open(filename, 'a')
    balance = 0
    new_balance = 0
    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open(filename, 'w+') as file2:
        if withdrawn_amount > balance:
            print('You have insufficient balance. Your balance is:', balance)
        else:
            new_balance = balance - withdrawn_amount
            new_balance = str(new_balance)
            file2.write(new_balance)
            print('Your new balance is:', new_balance)
            with open(transactionfilename, 'a') as file3:
                balance = str(balance)
                withdrawn_amount = str(withdrawn_amount)
                logging.basicConfig(filename=transactionfilename, level=logging.INFO, format='%(asctime)s %(message)s')
                logging.warning('is when this event was logged.')
                file3.write('Previous balance: ' + balance + '. Withdrawn amount is:' + withdrawn_amount + '. New balance:' + new_balance + '\n')
    file.close()
    opt()

def balance():
    username = input('Please enter username:')
    filename = username + '.txt'
    file = open(filename, 'a')
    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
        file.seek(0)
        if file.read(1):
            print('Your balance is:', balance)
        else:
            print('You have no balance left.')
    file.close()
    opt()

def choice():
    print('What would you like to do today? \n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Check Transaction History')
    m = int(input('Enter your choice:'))
    if (m == 1):
        depositcash()
    elif (m == 2):
        withdrawalcash()
    elif (m == 3):
        balance()
    elif (m == 4):
        transact()
    else:
        print('WRONG OPTION!!!')
        opt()

def opt():
    n = int(input('Do you want to continue? Select 0 to Continue, 1 to Terminate.'))
    if n == 0:
        choice()
    elif n == 1:
        end()
    else:
        print('WRONG OPTION!!!')
        opt()

def main():
    choose = int(input('ENTER YOUR CHOICE \n1.CREATE NEW USER ACCOUNT\n2.LOGIN TO EXISTING USER ACCOUNT\n3.TERMINATE SESSION\n--->'))
    if choose == 1:
        cnt = 1
        firstname = input('Enter First Name:')
        lastname = input('Enter Last Name:')
        address = input('Enter Address:')
        pin = input('ENTER A FOUR DIGIT PIN OF YOUR CHOICE:')
        username = firstname + lastname
        username_integer = username + str(cnt)
        with open('cust_profile.txt', 'r+') as f:
            data = f.read()
            if (username not in data):
                temp = username
                temp2 = pin
                f.write('Username:' + username + '\t' + 'Password:' + temp2 + '\t' + 'First Name:' + firstname + '\t' + 'Last Name:' + lastname + '\t' + 'Address:' + address + "\n")
                print("\nCreated username is:", temp, 'and pin number is', temp2, '\n')
            else:
                cnt = cnt + 1
                temp = username_integer
                temp2 = pin
                f.write('Username:' + username_integer + '\t' + 'Password:' + temp2 + 'First Name:' + firstname + '\t' + 'Last Name:' + lastname + '\t' + 'Address:' + address + "\n")
                print('\nCreated username is:', temp, 'and pin number is', temp2, "\n")
            main()
    elif choose == 2:
        print('Hello ! Welcome Customer !')
        print('Please insert your card and login to proceed.')
        cust_profile = open('cust_profile.txt', 'r')
        data = cust_profile.read()
        user = input('Please enter your username:')
        password = str(input('Please enter your pin number:'))
        if len(password) == 4:
            if user in data and password in data:
                print('Card Authenticated! Login Successfull!')
                opt()
            else:
                print('Incorrect Username or Pin number. Please try again later or contact our Customer Care Representative.')
                main()
        else:
            print('Incorrect Username or Pin number. Please try again later or contact our Customer Care Representative.')
            main()
    elif choose == 3:
        end()
    else:
        print('WRONG OPTION!')
print("****************************************************************************")
print("*                                                                          *")
print("*                   WELCOME TO A RANDOM ATM MACHINE                        *")
print("*                                                                          *")
print("****************************************************************************")
main()