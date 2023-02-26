import pandas as pd
import numpy as np

class Statistics():

    """This class contains all the functions to calculate save and retrieve statistics"""

    def __init__(self, df_path):
        self.df_path = df_path

    def load_df(self, df_path):
        df = pd.read_excel(df_path, index_col=0)

        return df

    def save_df(self, df, path_to_save):
        df.to_excel(path_to_save)

    def n_books_per_author(self, df):
        return df['author'].value_counts().rename_axis('author').reset_index(name='num_books')

    def n_books_per_publisher(self, df):
        return df['publisher'].value_counts().rename_axis('publisher').reset_index(name='num_books')

    def oldest_book(self, df):
        return df.iloc[[df['year_of_publication'].argmin()]] # I put 'df['year_of_publication'].argmin()' in a list so we get a DataFrame instead of a Series

    def youngest_book(self, df):
        return df.iloc[[df['year_of_publication'].argmax()]] # I put 'df['year_of_publication'].argmax()' in a list so we get a DataFrame instead of a Series

    def avg_age_of_books(self, df):
        now = np.datetime64('today')
        df_avg = pd.DataFrame({'average_age_of_books': [np.mean(now.astype(object).year - df['year_of_publication'])]})

        return df_avg

    def third_book_of_author_copy_number(self, df):

        df_copy_nums_of_third_book = df.sort_values('year_of_publication', ascending=False).groupby('author').nth(2).reset_index('author')
        df_copy_nums_of_third_book = df_copy_nums_of_third_book.loc[:,['author','copy_number']]

        return df_copy_nums_of_third_book

    def avg_time_to_library(self, df):

        #df.mean(df['date_added_to_the_library'].astype(object).year - df['year_of_publication']).groupby('author')

        #df.assign(avg_num=df.col2 - df.col1).groupby(['year', 'code'], as_index=False)['avg_num'].mean().round(2)
        df_copy = df.copy()
        df_copy['diff_time'] = df_copy['date_added_to_the_library'].dt.year - df_copy['year_of_publication']#.groupby(['author']).mean()
        df_avg_time_to_library = df_copy.groupby('author').agg(avg_time_to_library=('diff_time', np.mean)).reset_index('author')
        return df_avg_time_to_library


    def calc_and_save_all_stat(self):
        df = self.load_df(self.df_path)

        n_b_a = self.n_books_per_author(df)

        n_b_p = self.n_books_per_publisher(df)

        oldest = self.oldest_book(df)
        youngest = self.youngest_book(df)
        avg = self.avg_age_of_books(df)

        third_copy_num = self.third_book_of_author_copy_number(df)
        avg_time = self.avg_time_to_library(df)

        #self.third_book_of_author_copy_number(df)
        """
        print(n_b_a)
        print(n_b_p)
        print('oldest\n', oldest)
        print('youngest\n', youngest)
        print('average\n', avg)
        """

        self.save_df(oldest, 'oldest_book.xlsx')
        self.save_df(youngest, 'youngest_book.xlsx')
        self.save_df(avg, 'average_age_of_books.xlsx')
        self.save_df(n_b_p, 'num_books_per_publisher.xlsx')
        self.save_df(n_b_a, 'num_books_per_author.xlsx')
        self.save_df(third_copy_num, 'third_book_of_author_copy_number.xlsx')
        self.save_df(avg_time, 'avg_time_to_library.xlsx')

    def get_oldest_book(self):
        df = self.load_df('oldest_book.xlsx')
        print(df.to_string())
        return df

    def get_youngest_book(self):
        df = self.load_df('youngest_book.xlsx')
        print(df.to_string())
        return df

    def get_average_age_of_books(self):
        df = self.load_df('average_age_of_books.xlsx')
        print(df.to_string())
        return df

    def get_num_books_of_publisher(self, publisher):
        df = self.load_df('num_books_per_publisher.xlsx')
        df_n_books = df.loc[df['publisher'] == publisher]
        print(df_n_books)
        return df_n_books

    def get_num_books_of_author(self, author):
        df = self.load_df('num_books_per_author.xlsx')
        df_n_books = df.loc[df['author'] == author]
        print(df_n_books)
        return df_n_books

    def get_third_book_copy_num(self, author):
        df = self.load_df('third_book_of_author_copy_number.xlsx')
        df_third_copy_num = df.loc[df['author'] == author]
        print(df_third_copy_num)
        return df_third_copy_num

    def get_avg_time_to_library(self, author):
        df = self.load_df('avg_time_to_library.xlsx')
        df_avg_time = df.loc[df['author'] == author]
        print(df_avg_time)
        return df_avg_time
