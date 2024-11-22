from saveallbooks import saveallbooks
from viewallbooks import viewallbooks

def editbooks(all_books):
    viewallbooks(all_books)  # Display all books

    isbn = input("Enter the ISBN of the book to edit: ")

    for book in all_books:
        if str(book.get("isbn")) == isbn:
            print("\nEditing Book Details")
            print("Leave a field empty to keep its current value.")

            # Input new values
            new_title = input(f"Enter new title (current: {book['title']}): ") or book['title']
            new_author = input(f"Enter new author (current: {book['author']}): ") or book['author']
            new_year = input(f"Enter new publishing year (current: {book['year']}): ")
            new_price = input(f"Enter new price (current: {book['price']}): ")
            new_quantity = input(f"Enter new quantity (current: {book['quantity']}): ")

            # Update book details
            book['title'] = new_title
            book['author'] = new_author
            book['year'] = int(new_year) if new_year else book['year']
            book['price'] = float(new_price) if new_price else book['price']
            book['quantity'] = int(new_quantity) if new_quantity else book['quantity']

            saveallbooks(all_books)  # Save updated book list
            print(f"Book with ISBN {isbn} updated successfully.")
            return all_books

    print("This book isn’t available to edit.")
    return all_books
