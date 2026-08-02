from book import Book
from member import Member


class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.load_books()

    def add_book(self):

        isbn = input("Enter ISBN: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(isbn, title, author)

        self.books.append(book)
        self.save_books()

        print("\nBook added successfully!\n")

    def display_books(self):

        if len(self.books) == 0:
            print("\nNo books available.\n")
            return

        print("\n----- Book List -----")

        for book in self.books:

            status = "Available"

            if not book.available:
                status = "Borrowed"

            print(f"""
ISBN      : {book.isbn}
Title     : {book.title}
Author    : {book.author}
Status    : {status}
-----------------------------
""")

    def register_member(self):

        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")

        member = Member(member_id, name)

        self.members.append(member)

        print("\nMember registered successfully!\n")

    def display_members(self):

        if len(self.members) == 0:
            print("\nNo members registered.\n")
            return

        print("\n----- Member List -----")

        for member in self.members:

            print(f"""
Member ID : {member.member_id}
Name      : {member.name}
Borrowed Books : {len(member.borrowed_books)}
-----------------------------
""")

    def borrow_book(self):

        member_id = input("Enter Member ID: ")
        isbn = input("Enter Book ISBN: ")

        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if member is None:
            print("\nMember not found!\n")
            return

        if book is None:
            print("\nBook not found!\n")
            return

        if not book.available:
            print("\nBook is already borrowed!\n")
            return

        book.available = False
        member.borrowed_books.append(book)

        self.save_books()

        print("\nBook borrowed successfully!\n")

    def return_book(self):

        member_id = input("Enter Member ID: ")
        isbn = input("Enter Book ISBN: ")

        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if member is None:
            print("\nMember not found!\n")
            return

        for borrowed_book in member.borrowed_books:
            if borrowed_book.isbn == isbn:
                book = borrowed_book
                break

        if book is None:
            print("\nThis member has not borrowed this book!\n")
            return

        book.available = True
        member.borrowed_books.remove(book)

        self.save_books()

        print("\nBook returned successfully!\n")

    def save_books(self):

        with open("books.txt", "w") as file:

            for book in self.books:

                file.write(f"{book.isbn},{book.title},{book.author},{book.available}\n")

    def load_books(self):

        try:

            with open("books.txt", "r") as file:

                for line in file:

                    isbn, title, author, available = line.strip().split(",")

                    book = Book(isbn, title, author)

                    book.available = (available == "True")

                    self.books.append(book)

        except FileNotFoundError:
            pass