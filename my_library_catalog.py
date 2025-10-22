import os

#! lesson => use function in long prog as the main method in to built it
#! try all the method and use a good flow and plan to create a good prog and efficace


library_catalog = {}


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def add_book():
    while True:
        clear_terminal()
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter the author: ")
        library_catalog[isbn] = {"title" : title, "author" : author, "available" : True}

        print(f"book '{title}' by {author} added to the catalog with ISBN {isbn}.")
        choice = input("do you want to add another book? (y/n): ").lower()
        if choice != 'y':
            break

def check_out_book():

    while True:
        clear_terminal()
        isbn = input("Enter ISBN to check out: ") 
        if isbn in library_catalog:
            if library_catalog[isbn]["available"]:
                library_catalog[isbn]["available"] = False
                print(f"book '{library_catalog[isbn]['title']}' checked out successfully.")
            else:
                print("sorry, the book is currently checked out.")
        else:
            print("book not found in the catalog")
        choice = input("do you want to check out another book? (y/n): ").lower()
        if choice != 'y':
            break

def check_in_book():
    while True:
        clear_terminal()
        isbn = input("Enter ISBN to check in: ")
        if isbn in library_catalog:
            if not library_catalog[isbn]["available"]:
                library_catalog[isbn]["available"] = True
                print(f"book '{library_catalog[isbn]['title']}' checked in successfully.")
            else:
                print("the book is already available in the library.")
        else:
            print('book not found in the catalog.')
        choice = input("do you want to check in another book? (y/n): ").lower()
        if choice != 'y':
            break


def list_books():
    while True:
        clear_terminal()
        print("\nlibrary catalog:")
        for isbn in library_catalog:
            book_info = library_catalog[isbn]
            print(f"ISBN:{isbn}, title:{book_info['title']}, author:{book_info['author']}")
        choice = input("do you want to go back to the main menu? (y/n): ").lower()
        if choice != "y":
            break

while True:
    print("\nMenu:")
    print("1. Add book")
    print("2. check out book")
    print("3. check in book")
    print("4. list books")
    print("5. exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_book()
    
    elif choice == "2":
        check_out_book()
    
    elif choice == "3":
        check_in_book()
    
    elif choice == "4":
        list_books()
    
    elif choice == "5":
        print("Exiting program.")
        break
    
    else:
        print("wrong choice 🕷")