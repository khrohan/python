import addbooks
import viewallbooks
import removebooks
import editbooks
import lentbooks

all_books = []

while True: 
    print("Welcome to library")
    print("0. Exit.")
    print("1. Add A New Books.")
    print("2. View All Book.")
    print("3. Remove a book.")
    print("4. Edit a book.")
    print("5. Lending books")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library ")
        break
    elif menu == "1":
        all_books = addbooks.addbooks(all_books)
        

    elif menu == "2":
        viewallbooks.viewallbooks(all_books)
    
    elif menu == "3":
        removebooks = removebooks.removebooks(all_books)
    
    elif menu == "4":
        editbooks = editbooks.editbooks(all_books)

    elif menu == "5":
        lentbooks.lentbooks(all_books)

    else: 
        print("Choose a valid code")  

        