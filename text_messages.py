
class Messages:

    @staticmethod
    def intro_message():
        print("Welcome to the Book Library!")

    @staticmethod
    def authentication_messages():
        print("'log_in' - access your account.\n"
              "'sign_up' - create a new account.\n"
              "'exit' - exits the application.\n")

    @staticmethod
    def options_message():
        print("'add_book' - adds a new book to your inventory.\n"
              "'finished_books' - shows you the book you have already read.\n"
              "'borrowed_books' - shows you the books you have borrowed.\n"
              "'show_inventory' - shows you all the books in your inventory\n\n."
              "'log_out' - logs you out.\n"
              "'exit' - exits the application.\n")
