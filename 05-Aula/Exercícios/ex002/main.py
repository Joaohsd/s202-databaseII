from db.database import Database
from model.bookModel import BookModel

def main():
    db = Database(database="library", collection="books")
    bookModel = BookModel(db)
    # Create
    bookId = bookModel.create_book(title='Crônicas de Nárnia', author='C. S. Lewis', year=1954, price=30.0)
    # Read
    bookRead = bookModel.read_book_by_id(book_id=bookId)
    # Update
    bookModifiedId = bookModel.update_book(book_id=bookId, title="1984", author="George Orwell", year=1949, price=20.0)
    #Delete
    bookDeletedId = bookModel.delete_book(book_id=bookId)

if __name__ == "__main__":
    main()
