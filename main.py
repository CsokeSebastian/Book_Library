from text_messages import *
from authentication import *
from app_function import *


# 1. Create the welcoming message
# 2. Create the menu
# 2.1. Create the buttons for the menu
# 3 create the json file with books read, books borrowed, books that I am reading now, all the books
# Maintain the record of BookStartDate and BookEndDate
# Features:
# List books
# Add books
# Update book
# Share
# Data/System Design
# Data storage: Json files, comma separated

ADD_BOOK_COMMAND = "add_book"
BORROWED_BOOKS = "borrowed_books"
NOW_READING_BOOKS = "reading_now"
FINISHED_BOOKS = "finished_books"
SHOW_BOOK_INVENTORY = "show_inventory"
LOGIN_COMMAND = "log_in"
LOGOUT_COMMAND = "log_out"
EXIT_COMMAND = "exit"
ADD_NEW_USER_COMMAND = "sign_up"
IS_USER_LOGGED_IN = False

# must_login()
Messages.intro_message()
Messages.authentication_messages()
Messages.options_message()

while True:
    command = input("Enter your command: ").lower()
    if command == EXIT_COMMAND:
        break
    elif command == ADD_NEW_USER_COMMAND:
        add_new_user()
    elif command == LOGIN_COMMAND:
        IS_USER_LOGGED_IN = must_login(IS_USER_LOGGED_IN)
    elif command == LOGOUT_COMMAND:
        logout(IS_USER_LOGGED_IN)
    if not IS_USER_LOGGED_IN:
        # pass
        Messages.not_logged_in_message()
        continue
    elif command == ADD_BOOK_COMMAND:
        add_new_book()
    elif command == SHOW_BOOK_INVENTORY:
        see_book_inventory()
    elif command == BORROWED_BOOKS:
        pass
    elif command == FINISHED_BOOKS:
        pass
    elif command == NOW_READING_BOOKS:
        pass
