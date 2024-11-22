from saveallbooks import saveallbooks
from viewallbooks import viewallbooks

def removebooks(all_books):
    viewallbooks(all_books)

    isbn = input("Enter the ISBN of the book to remove: ")

    for book in all_books:
        if str(book.get("isbn")) == isbn:  
            all_books.remove(book)
            saveallbooks(all_books) 
            print(f"Book with ISBN {isbn} removed successfully.")
            return all_books

    print("This book isn’t available to remove.")
    return all_books
