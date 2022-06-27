import re


def login():
    print("************LOGIN************")
    count = 0
    userDb = None
    try:
        userDb = open("userDataBase.txt", "r")
    except:
        userDb = open("userDataBase.txt", "w+")

    usrName = input("Email/Username: ")
    passWd = input("Password: ")

    for i in userDb:
        email, regPwd = i.split("|")
        regPwd = regPwd.strip()
        if usrName == email:
            count += 1
            authenticate(regPwd, passWd)
            break

    if count == 0:
        wantToRegister = input("It seems you don't have an account. Do you want to register?\nY ==> Yes\nN ==> No "
                               "\nEnter your choice: ")
        if wantToRegister == "y" or wantToRegister == "y":
            userDb.close()
            register()


def authenticate(regPwd, pWd):
    if regPwd == pWd:
        print("Login success!")
    else:
        print("Invalid username or password")
        print("1 ==> Enter your password again\n2 ==> Forgot password?")
        usrOption = input("Enter the choice: ")
        if usrOption == "1":
            passWd = input("Password: ")
            authenticate(regPwd, passWd)
        elif usrOption == "2":
            print("Your password is: " + regPwd)
        else:
            print("Invalid option. Exiting...")


def register():
    print("************REGISTRATION************")
    userDb = open("userDataBase.txt", "r")

    while True:
        usrName = input("Email address: ")
        emailVerified = verifyEmail(usrName)

        if emailVerified:
            break
        else:
            print("Invalid email address. Please enter a valid email address")

    while True:
        password = input("Password: ")
        passVerified = checkpasswd(password)

        if passVerified:
            break
        else:
            print("Password did not match criteria. Please enter a valid password")

    while True:
        conPassword = input("Confirm password: ")

        if password == conPassword:
            break
        else:
            print("Password did not match. Enter again")

    userDb = open("userDatabase.txt", "a")
    userDb.write(usrName + "|" + password + "\n")
    userDb.close()
    print("Registration Successful! Plesae login to your account")
    login()


def verifyEmail(email):
    regex = r'[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{3,}\b'

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def checkpasswd(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,16}$"
    if re.fullmatch(regex, password):
        return True
    else:
        return False


def signin_app():
    print("Task1")
    while True:
        print("Choose your option: ")
        print("1 ==> Login")
        print("2 ==> Register")
        print("0 ==> Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            login()
            break
        elif choice == 2:
            register()
            wantToLogin = input("Do you want to login? \nY ==> Yes \nN ==> No\n Enter your choice here: ")
            if wantToLogin.upper() == "Y":
                login()
            else:
                break
        elif choice == 0:
            print("--------- Execution End------")
            break
        else:
            print("Invalid choice. Please enter a valid choice")


if __name__ == '__main__':
    signin_app()
