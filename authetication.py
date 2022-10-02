IS_USER_LOGGED_IN = False


def create_new_account():
    print("Create new account")
    user = input("Enter a username: ")
    password = input("Enter a password: ")
    file = open("users.json", "a")
    file.write(f"{user},{password}\n")
    print(f"Your username is: {user}\nYour password is: {password}")


def login(user, password):
    file = open('users.json', 'r')
    for line in file:
        data = line.split(',')
        user_name = data[0]
        user_password = data[1]
        if user == user_name and password == user_password:
            file.close()
            return True
    file.close()
    return False


def must_login():
    global IS_USER_LOGGED_IN
    if IS_USER_LOGGED_IN:
        print("You are already logged in!")
    else:
        print("You need to log in!")
        user_name = input('Please insert username: ')
        user_password = input('Please insert password: ')
        if login(user_name, user_password):
            IS_USER_LOGGED_IN = True
            print("User has logged in!")
        else:
            print("Try again, username/password incorrect!")


def logout():
    global IS_USER_LOGGED_IN
    IS_USER_LOGGED_IN = False
    print("You have been logged out!")
