import subprocess
import time
import os
def consl():
    print("deb console v0.7")
    command = input("$ {}".format(UserName))
    if command == 'version--':
        print("debOS v0.2.0(Black Sky)")
    if command == '?':
        print("Commands : version--(shows version), ?(Shows command list)")

def doesFileExists(filePathAndName):
            return os.path.exists(filePathAndName)
Q1 = input("""
DEB OS
LOG IN
[1]. Sign In To Current Account.
[2]. Sign Up (Will Replace Old User If An Account Is Already Set-Up)
""")

if Q1 == '2':
    Password = input('Please Enter Your Password: ')
    while True:

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
            print('A new Account was Created! The Program will Now Shutdown')
            time.sleep(1.10)
            break





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
                [4]. Calculator
                [3]. Console
                [2]. Browser
                [1]. Exit OS
                """)
        if MainMenu == '1':
            break
        if MainMenu == '2':
            subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')
        if MainMenu == '3':
            consl()
        if MainMenu == '4':
            subprocess.Popen('C:\Windows\System32\calc.exe')
    else:
        print('Access Denied')
        print('The OS Will Now Shutdown!')
        time.sleep(1.15)
        exit()
