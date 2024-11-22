from saveallbooks import saveallbooks
from viewallbooks import viewallbooks

def lentbooks(all_books, lent_books_file="lent_books.csv"):
    viewallbooks(all_books)

    isbn = input("Enter the ISBN of the book to lend: ")
    borrower = input("Enter the name of the borrower: ")

    for book in all_books:
        if str(book.get("isbn")) == isbn:
            if book["quantity"] > 0:
                
                book["quantity"] -= 1

            
                with open(lent_books_file, "a") as file:
                    file.write(f"{isbn},{book['title']},{borrower}\n")

                
                saveallbooks(all_books)

                print(f"Book '{book['title']}' lent to {borrower}. Quantity updated.")
                return
            else:
                print("Not enough copies of the book available to lend.")
                return

    print("This book isn’t available in the library.")

