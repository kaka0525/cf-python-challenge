class Library(object):
    def __init__(self, name, shelves=None):
        self.shelves = shelves or []
        self.name = name

    def report_shelf(self):
        print self.name + " has " + str(len(self.shelves)) + " shelves."

    def report_books(self):
        for shelf in self.shelves:
            shelf.report_books()


class Shelf(object):
    def __init__(self, name, books=None):
        self.books = books or []
        self.name = name

    def report_books(self):
        print self.name + " has " + ", ".join(book.title
                                              for book in self.books)


class Book(object):
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title == other.title

    def enshelf(self, shelf):
        shelf.books.append(self)

    def unshelf(self, shelf):
        shelf.books.remove(self)


SPU = Library("SPU")
shelf_one = Shelf("shelf_one")
shelf_two = Shelf("shelf_two")
SPU.shelves.append(shelf_one)
SPU.shelves.append(shelf_two)
Book("Harry Potter").enshelf(shelf_one)
Book("Kite Runner").enshelf(shelf_one)
Book("Who move my cheese").enshelf(shelf_one)
Book("Cook Book").enshelf(shelf_two)
Book("Bartending Book").enshelf(shelf_two)
Book("Life of Pi").enshelf(shelf_two)
Book("Cook Book").unshelf(shelf_two)
SPU.report_books()
SPU.report_shelf()
shelf_two.report_books()
