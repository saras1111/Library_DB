import pandas as pd
import os
import numpy as np

class Library():

    """This class contains the functions to create Library database, add books and search books"""

    def __init__(self, df_path):
        self.df_path = df_path

    def create_empty_df(self):
        df = pd.DataFrame()

        return df

    def save_df(self, df):
        df.to_excel(self.df_path)

    def load_df(self):
        df = pd.read_excel(self.df_path, index_col=0)

        return df

    def add_book(self, book, statistics):
        '''used to add books to the library'''
        
        if not os.path.exists(self.df_path):
            df = self.create_empty_df()
            df = df.append(book, ignore_index = True)
        else:
            df = self.load_df()

            if df.empty:
                df = df.append(book, ignore_index = True)
            else:
                if not ((df['title'] == book['title']) & (df['author'] == book['author']) & (df['publisher'] == book['publisher']) & (df['year_of_publication'] == book['year_of_publication'])).any():
                    df = df.append(book, ignore_index = True)
                else:
                    # if book already in df, we increase copy number, and choose the first data ad 'date_added_to_the_library'
                    ind = df[(df['title'] == book['title']) & (df['author'] == book['author']) & (df['publisher'] == book['publisher']) & (df['year_of_publication'] == book['year_of_publication'])].index.tolist()
                    df.loc[ind, 'copy_number'] += book['copy_number']
                    if np.datetime64(book['date_added_to_the_library']) < df.loc[ind, 'date_added_to_the_library'].values[0]:
                        df.loc[ind, 'date_added_to_the_library'] = book['date_added_to_the_library']
        self.save_df(df)

        print("Modified table saved to file")

        # statistics are recalculated every time a book is added
        statistics.calc_and_save_all_stat()
        print("All statistics were recalculated and saved to file")

    def search_book(self, *,  title=None, author=None, publisher=None, year_of_publication=None, date_added_to_the_library=None, copy_number=None):
        # accepts keyword only arguments
        # doing the filtering for all the attributes provided by the user

        df = self.load_df()

        if title:
            df =  df.loc[df['title'] == title]
        if author:
            df =  df.loc[df['author'] == author]
        if publisher:
            df =  df.loc[df['publisher'] == publisher]
        if year_of_publication:
            df =  df.loc[df['year_of_publication'] == year_of_publication]
        if date_added_to_the_library:
            df =  df.loc[df['date_added_to_the_library'] == date_added_to_the_library]
        if copy_number:
            df =  df.loc[df['copy_number'] == copy_number]
        return df
