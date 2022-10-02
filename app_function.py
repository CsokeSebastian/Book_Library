import json


def add_new_book():
    print("Here you can add new books to your inventory.")
    author = input("Enter the authors name: ")
    title = input("Enter the books title: ")
    book = {"Title": title,
            "Author": author}
    dumped_data = json.dumps(book)
    file = open("book_inventory.json", "a")
    file.write(dumped_data)
    file.close()
    print(f"The book '{title}' by {author}, is now in your inventory.")


def see_book_inventory():
    print("This is your inventory: \n")
    file = open("book_inventory.json", "r")
    inventory = json.load(file)
    file.close()
    return inventory
