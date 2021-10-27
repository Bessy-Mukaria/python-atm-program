# Prompt the user for a password without echoing
import getpass


def init():
    # Customers Nested Dict
    global customersDict
    customersDict = {1: {'username': 'trial', 'pin': 0000, 'balance': {'KSH': 140, 'USD': 0}},
                     2: {'username': 'Kahalf', 'pin': 1111, 'balance': {'KSH': 3000, 'USD': 220}},
                     3: {'username': 'Ibrahim', 'pin': 2222, 'balance': {'KSH': 140, 'USD': 1000}},
                     4: {'username': 'Makena', 'pin': 3333, 'balance': {'KSH': 2440, 'USD': 20}},
                     5: {'username': 'Kendi', 'pin': 4444, 'balance': {'KSH': 13000, 'USD': 650}},
                     6: {'username': 'Mwende', 'pin': 5555, 'balance': {'KSH': 14000, 'USD': 230}},
                     7: {'username': 'Ephraim', 'pin': 6666, 'balance': {'KSH': 240, 'USD': 100}},
                     8: {'username': 'Brian', 'pin': 7777, 'balance': {'KSH': 80, 'USD': 10}},
                     9: {'username': 'Sam', 'pin': 8888, 'balance': {'KSH': 160, 'USD': 30}}}

    print('*******************************************\n')
    print('**************WELCOME TO AZUBI ATM**********\n')
    print('********************************************\n')

    account = int(input('Do you have an account with AZUBI BANK? 1. (Yes) or 2. (No): '))
    if account == 1:
        accounts()
    elif account == 2:
        print('\n*****************************************\n')
        print('Please consider visiting your nearest Branch\n')
        print('*********************************************\n')

        init()


def accounts():
    global user
    user = input('Please Enter Your Username: ').capitalize()
    # user.capitalize()
    count = 0
    outer_key = []
    for keys in customersDict:
        count += 1
        outer_key.append(keys)

    # Existing Usernames
    inner_keys = []
    for k in customersDict:
        inner_key = customersDict[k]['username']
        inner_keys.append(inner_key)

    for i in outer_key:
        if user in customersDict[i]['username']:
            authentication(i)
    if user not in inner_keys:
        print('\n*************************************\n')
        print('Incorrect Username. Please try again\n')
        print('*************************************\n')
        init()


def authentication(n):
    global key
    key = n
    PIN = getpass.getpass('Please Enter your PIN: ')
    if int(PIN) == customersDict[key]['pin']:
        print('\n**********************************\n')
        print(f'WELCOME {user} To AZUBI ATM SERVICES\n')
        print('***************************************')
        services()
    else:
        print('Incorrect Password, Please try again')
        attempts = 0
        while attempts < 2:
            PIN = getpass.getpass('Please Enter your PIN: ')
            attempts += 1
        else:
            print('**********************************\n')
            print('***3 UNSUCCESSFUL PIN ATTEMPTS!***\n')
            print('\tACCOUNT LOCKED!!\n')
            print('***********************************\n')


def services():
    option = int(
        input('Please select how we may be of service to you Today\n1.CHECK BALANCE:\n2.WITHDRAWAL:\n3.LOGOUT:\n'))
    balances = customersDict[key]['balance']
    ksh = customersDict[key]['balance']['KSH']
    usd = customersDict[key]['balance']['USD']

    Balance_Ksh = ksh + (usd * 100)
    Balance_USD = (ksh / 100) + usd
    # Balance Check
    if option == 1:
        currency = int(input('Please select Currency: 1.KSH, 2.USD: '))
        if currency == 1:
            print('\n-------------------------------------------\n')
            print(f'Your Account balance in KSH is: {Balance_Ksh}')
            print('\n--------------------------------------------\n')

            service2 = int(input('Do you want to perform another service? 1.YES 2.NO: '))
            if service2 == 1:
                services()
            elif service2 == 2:
                print('\n----------------------------------\n')
                print('Thank you for Banking with us\n')
                print('\n-----------------------------------\n')
                init()

        elif currency == 2:
            print('\n-------------------------------------------\n')
            print(f'Your Account balance in USD is: {Balance_USD}')
            print('\n--------------------------------------------\n')

            service2 = int(input('Do you want to perform another service? 1.YES 2.NO: '))
            if service2 == 1:
                services()
            elif service2 == 2:
                print('\n----------------------------------\n')
                print('Thank you for Banking with us\n')
                print('\n-----------------------------------\n')
                init()
    # Withdrawal
    elif option == 2:
        currency = int(input('Please select Currency: 1.KSH, 2.USD: '))

        # KSH
        if currency == 1:
            amount = int(input('How Much Do you want to withdraw in KSH: '))
            if amount <= Balance_Ksh:
                new_Balance = Balance_Ksh - amount
                receipt = int(input('Do you want a printed receipt? 1.YES 2.NO: '))
                if receipt == 1:
                    print('\n-------------------------------------------\n')
                    print(f'You have withdrawn KSH: {amount}\n')
                    print(f'Your Account Balance is KSH: {new_Balance}')
                    print('\n--------------------------------------------\n')

                    service2 = int(input('Do you want to perform another service? 1.YES 2.NO: '))
                    if service2 == 1:
                        services()
                    elif service2 == 2:
                        print('\n----------------------------------\n')
                        print('Thank you for Banking with us\n')
                        print('\n-----------------------------------\n')
                        init()

                elif receipt == 2:
                    service2 = int(input('Do you want to perform another service? 1.YES 2.NO: '))
                    if service2 == 1:
                        services()
                    elif service2 == 2:
                        print('\n----------------------------------\n')
                        print('Thank you for Banking with us\n')
                        print('\n-----------------------------------\n')
                        init()

            elif amount > Balance_Ksh:
                print('Insufficinet Balance to Complete the transaction')
                services()


        # USD Withdrawal
        elif currency == 2:
            amount = int(input('How Much Do you want to withdraw in USD: '))
            if amount <= Balance_USD:
                new_Balance = Balance_USD - amount
                receipt = int(input('Do you want a printed receipt? 1.YES 2.NO: '))
                if receipt == 1:
                    print('\n-------------------------------------------\n')
                    print(f'You have withdrawn USD: {amount}\n')
                    print(f'Your Account Balance is USD: {new_Balance}')
                    print('\n--------------------------------------------\n')

                    service2 = int(input('Do you want to perform another service? 1.YES 2.NO: '))
                    if service2 == 1:
                        services()
                    elif service2 == 2:
                        print('\n----------------------------------\n')
                        print('Thank you for Banking with us\n')
                        print('\n-----------------------------------\n')
                        init()

                elif receipt == 2:
                    service2 = int(input('Do you want to perform another service? 1.YES 2.NO: '))
                    if service2 == 1:
                        services()
                    elif service2 == 2:
                        print('\n----------------------------------\n')
                        print('Thank you for Banking with us\n')
                        print('\n-----------------------------------\n')
                        init()

            elif amount > Balance_USD:
                print('Insufficinet Balance to Complete the transaction')
                services()

    elif option == 3:
        print('\n----------------------------------\n')
        print('Thank you for Banking with us\n')
        print('\n-----------------------------------\n')
        init()


init()