import pandas as pd


def get_publisher(conn):
    return pd.read_sql("SELECT * FROM publisher", conn)


def get_author(conn):
    return pd.read_sql("SELECT * FROM author", conn)


def get_genre(conn):
    return pd.read_sql("SELECT * FROM genre", conn)


def get_card(conn, publishers, genres, authors):
    return pd.read_sql(f'''
        SELECT
        	title AS 'Название',
        	group_concat(DISTINCT author_name) AS 'Авторы',
        	genre_name AS 'Жанр',
        	publisher_name AS 'Издательство',
            year_publication AS 'Год_издания',
            available_numbers AS 'Количество'
        FROM book
        JOIN genre USING(genre_id)
        JOIN publisher USING(publisher_id)
        JOIN book_author USING(book_id)
        JOIN author USING(author_id)
        GROUP BY book_id
        HAVING (genre_id IN {genres} OR {not genres})
            AND (publisher_id IN {publishers} OR {not publishers})
            AND (author_id IN {authors} OR {not authors})
        ORDER BY
            title,
            available_numbers DESC,
            genre_name,
            year_publication DESC 
    ''', conn)