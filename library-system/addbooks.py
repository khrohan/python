# title, authors, ISBN, publishing year, price and quantity
from saveallbooks import saveallbooks
def addbooks(all_books):
    title = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    isbn = str(input("Enter ISBN Number: "))
    year = int(input("Enter Publishing year: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity Number: "))

    book = {
        "title" : title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }

    all_books.append(book)
    saveallbooks(all_books)

    print("books added successfully")

    return all_books
