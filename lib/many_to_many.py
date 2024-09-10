class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set([contract.author for contract in self.contracts()]))

    def __repr__(self):
        return f"Book(title='{self.title}')"


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"Author(name='{self.name}')"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return (f"Contract(author={self.author}, book={self.book}, "
                f"date='{self.date}', royalties={self.royalties})")

# Example Usage:

# Create Author and Book
author = Author("John Doe")
book1 = Book("Book One")
book2 = Book("Book Two")

# Author signs a contract for the books
contract1 = author.sign_contract(book1, "2024-01-01", 10)
contract2 = author.sign_contract(book2, "2024-02-01", 15)

# Get total royalties earned
print(f"Total Royalties: {author.total_royalties()}%")

# Find contracts by date
contracts_on_jan1 = Contract.contracts_by_date("2024-01-01")
print(f"Contracts on 2024-01-01: {contracts_on_jan1}")

# Get books and contracts related to the author
print(f"Books by {author.name}: {author.books()}")
print(f"Contracts of {author.name}: {author.contracts()}")

# Get contracts and authors related to the book
print(f"Contracts of {book1.title}: {book1.contracts()}")
print(f"Authors of {book1.title}: {book1.authors()}")
