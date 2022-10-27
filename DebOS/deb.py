import time
import os
Q1 = input("""
DEB OS
LOG IN
[1]. Sign In To Current Account.
[2]. Sign Up (Will Replace Old User If An Account Is Already Set-Up)
""")

if Q1 == '2':
    Password = input('Please Enter Your Password: ')
    while True:
        def doesFileExists(filePathAndName):
            return os.path.exists(filePathAndName)

        if doesFileExists('./Password.txt'):
            with open('Password.txt') as f:
                contents = f.read()
            if contents == Password:
                UserNameS = input('Please Enter Your New Username: ')
                PasswordS = input('Please Enter Your New Password: ')
                with open('Username.txt', 'w') as f:
                    f.write(UserNameS)
                with open('Password.txt', 'w') as f:
                    f.write(PasswordS)
                    break
        else:
            with open('Password.txt', 'w') as f:
                f.write(Password)
            print('Password.txt Was Created! The Program will Now Shutdown')
            time.sleep(1.10)
            exit()





if Q1 == '1':
    UserName = input('Please Enter Your Username: ')
    Password = input('Please Enter Your Password: ')


    with open('Username.txt') as f:
        contents = f.read()
    with open('Password.txt') as f:
        contents = f.read()
while True:
    if contents == Password:
        print('Login Successful')
        time.sleep(1)
        print('Welcome To DEB OS, {}'.format(UserName))
        MainMenu = input("""
                What Would You Like To Do?
                [2]. Browser
                [1]. Exit OS
                """)
        if MainMenu == '1':
            break
        if MainMenu == '2':
            print("The feature in progress.")
            time.sleep(1)
            break
    else:
        print('Access Denied')
        print('The Program Will Now Shutdown!')
        time.sleep(1.15)
        exit()
