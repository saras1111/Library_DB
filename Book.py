
class Book():

    """This is a class to create books, that can be added to the library"""

    def __init__(self, title, author, publisher, year_of_publication, date_added_to_the_library, copy_number):
        self.title = title
        self.author =  author
        self.publisher = publisher
        self.year_of_publication = year_of_publication
        self.date_added_to_the_library = date_added_to_the_library
        self.copy_number = copy_number

    def get_book(self):
        '''returns data of a book in a dictionary book - so it can be easily added to the library'''

        return {'title' : self.title,
                'author' :  self.author,
                'publisher' : self.publisher,
                'year_of_publication' : self.year_of_publication,
                'date_added_to_the_library' : self.date_added_to_the_library,
                'copy_number' : self.copy_number}
