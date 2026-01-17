class Book:
    result = []

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.result.append(
            f"The title: {self.title}, Author Name: {self.author}"
        )

    @classmethod
    def get_result(cls):
        return cls.result


n = int(input("Enter the Number of Books: "))

for i in range(n):
    title = input("Enter the Book Name: ").strip()
    name = input("Enter the Author Name: ").strip()
    Book(title, name)

for book_info in Book.get_result():
    print(book_info)
