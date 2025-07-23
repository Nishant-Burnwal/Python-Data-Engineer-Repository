"""
1. View Library
2. Buy book
3. rent book
4. Delete book
5. Issue limit 3 books per month

bookstore
view books 
"""

# class library
class Library:
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books
        self.rented_books_count = {}

    def view_books(self):
        print("Available Books: ")
        for book in self.list_of_books:
            print(f"{book}")
        else:
            print("No book available.")
        

    def buy_book(self, title):

        if title in self.list_of_books:
            print(f"Book {title} bought.")
            self.list_of_books.remove(title)
        else:
            print(f"Book {title} not found.")

    def rent_book(self, user_name, title):
        if title not in self.list_of_books:
            print(f"Book {title} not found or already rented.")
            return
        user_rented = self.rented_books_count.get(user_name, [])
        if len(user_name) >= 3:
            print(f"{user_name} has reached 3 book limit per month.")
            return
        self.list_of_books.remove(title)
        user_rented.append(title)
        self.rented_books_count[user_name] = user_rented
        print(f"{user_name} rented '{title}'. Total rented this month: {len(user_rented)}")

    def delete_book(self, title):
        if title in self.list_of_books:
            self.list_of_books.remove(title)
            print(f"Book: {title} deleted.")
        else:
            print(f"Book '{title}' not found or already rented.")
        


def main():
    initial_books = ["Book A", "Book B", "Book C", "Book D", "Book E", "Book F", "Book G", "Book H", "Book I", "Book J"]
    lib = Library(initial_books)
    lib.view_books()

    lib.buy_book("Book A")
    lib.rent_book("Rahul", "Book B")
    lib.rent_book("Ravi", "Book C")
    lib.rent_book("Alice", "Book D")
    lib.rent_book("Alice", "Book X")
    lib.rent_book("Alex", "Book A")
    lib.rent_book("Alice", "Book B")
    
    lib.view_books()

    lib.view_books()

    lib.delete_book("Book H")
    lib.delete_book("Book B")

    lib.view_books()


if __name__ == "__main__":
    main()