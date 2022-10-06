import json



def add_new_user():
    user_name = input("Enter a user name: ")
    user_password = input("Enter a password: ")
    user = {"client":
                {"Username": user_name,
                 "Password": user_password}}
    dumped_data = json.dumps(user)
    file = open("users.json.", "a")
    file.write(dumped_data)
    file.close()
    print(f"Your user name is '{user_name}' and {user_password} is your password.")


def login(user, password):
    with open("users.json", "r") as file:
        data = json.load(file)
        user_name = data["Username"]
        user_password = data["Password"]
        if user == user_name and password == user_password:
            return True
        else:
            return False


def must_login(IS_USER_LOGGED_IN):
    if IS_USER_LOGGED_IN:
        print("You are already logged in!")
        # return True
    else:
        print("You need to log in!")
        user_name = input('Please insert username: ')
        user_password = input('Please insert password: ')
        if login(user_name, user_password):
            IS_USER_LOGGED_IN = True
            print("User has logged in!")
            return True
        else:
            print("Try again, username/password incorrect!")
            return False


def logout(IS_USER_LOGGED_IN):
    IS_USER_LOGGED_IN = False
    print("You have been logged out!")
    return False
