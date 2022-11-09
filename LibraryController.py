from jinja2 import Template
import sqlite3
from LibraryModel import get_publisher, get_author, get_genre, get_card
# задаем id читателя, для которого формируем страницу
genresIds = (1, 2, 3)
authorsIds = (1, 2, 3, 4, 5)
publishersIds = ()
# устанавливаем соединение с базой данных
conn = sqlite3.connect("library.sqlite")
df_author = get_author(conn)
df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_card = get_card(conn, publishersIds, genresIds, authorsIds)

# закрываем соединение с базой
conn.close()
# открываем файл indexTemplate.html и читаем шаблон
f_template = open('template/indexTemplate.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
 authors=df_author,
 publishers=df_publisher,
 genres=df_genre,
 card=df_card,
 selectedAuthors = authorsIds,
 selectedPublisers = publishersIds,
 selectedGenres = genresIds,
 len = len
 )
#создаем файл для HTML-страницы
f = open('index.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()