import json
from text_messages import *


# # # # just like the bank app you did before

# 1. Create the welcoming message
# 2. Create the menu
# 2.1. Create the buttons for the menu
# 3 create the json file with books read, books borrowed, books that i am reading now, all the books
# Maintain the record of BookStartDate and BookEndDate
# Features:
# List books
# Add books
# Update book
# Share
## Data/System Design
# Data storage: Json files, comma separated

ADD_BOOK_COMMAND = "add_book"
BORROWED_BOOKS = "borrowed_books"
FINISHED_BOOKS = "finished_books"
SHOW_BOOK_INVENTORY = "show_inventory"
LOGIN_COMMAND = "log_in"
LOGOUT_COMMAND = "log_out"
EXIT_COMMAND = "exit"
ADD_USER_COMMAND = "sign_up"



Messages.intro_message()

