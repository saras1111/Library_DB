from Book import Book
import datetime

from Library import Library
from FillDatabase import fill_data_base
from Statistics import Statistics

''' instantiating Book class with specific data of a book'''
book1=Book('alma', 'Saci', 'PLOS', 2021, datetime.date(2023, 2, 25), 3)
'''get the dictionary containing the data of a book - this will be used to add the specific book to the library'''
book1_dict = book1.get_book()

print(book1_dict)

'''Instantiating our library class and trying some of its functions'''
library = Library('./Library.xlsx')
df = library.create_empty_df()
library.save_df(df)
print(df)

'''Instantiating the Statistics class'''
statistics = Statistics('./Library.xlsx')


'''Adding some books to the library'''
library.add_book(book1_dict, statistics)

book2 = Book('körte', 'Saci', 'PLOS', 2022, datetime.date(2023, 1, 25), 1)

library.add_book(book2.get_book(), statistics)

library.add_book(Book('banán', 'Kata', 'PLOS', 2019, datetime.date(2022, 1, 25), 1).get_book(), statistics)

library.add_book(Book('mango', 'Saci', 'PLOS', 2020, datetime.date(2021, 1, 25), 1).get_book(), statistics)

fill_data_base(library, statistics)

''' try searching books by different combination of attributes'''
found = library.search_book(title='alma')
print(found.to_string()) # for prettier print

found = library.search_book(author = 'Saci')
print(found.to_string()) # for prettier print

found = library.search_book(title='alma', author = 'Saci')
print(found.to_string()) # for prettier print

''' run the calculation and save of all the implemented statistics. This is also done whenever a new book is added to the library'''
statistics.calc_and_save_all_stat()

'''retrieve statistics results '''
df_oldest = statistics.get_oldest_book()
df_youngest = statistics.get_youngest_book()
df_avg = statistics.get_average_age_of_books()
df_nbp = statistics.get_num_books_of_publisher('PLOS')
df_nba = statistics.get_num_books_of_author('Saci')
df_third_copy_num = statistics.get_third_book_copy_num('Saci')
df_avg_time_to_lb = statistics.get_avg_time_to_library('Saci')
