import mysql.connector

# Параметри для подключения чтения из таблиц с фильмами
dbconfig_R = {'host': '',
            'user': '',
            'password': '',
            'database': ''}

# select all genres in database
def select_genres(csr):
    csr.execute("SELECT GROUP_CONCAT(genres) FROM movies")
    result = csr.fetchall()
    l = result[0][0]
    result = list(set(l.split(','))) # разделаем список, делаем множество уникальных
    return result

# select 10 movies by genre
def select_films_genres_10(csr, gen):
    request = f"""SELECT title, runtime, year, genres FROM movies 
    WHERE genres LIKE '%{gen}%' LIMIT 10 """
    print(request)
    csr.execute(request)
    films = csr.fetchall()
    return films

# select availible years in database
def select_years(csr):
    csr.execute("SELECT year FROM movies GROUP BY year ORDER BY year")
    result = [x[0] for x in csr.fetchall()]
    return result

# select 10 movies from year
def select_by_year_10(csr, yr):
    request = f"""SELECT title, runtime, year, genres FROM movies 
    WHERE year LIKE '%{yr}%' LIMIT 10"""
    csr.execute(request)
    films = csr.fetchall()
    return films

# select 10 movies by genre and from year
def select_films_genres_and_year_10(csr, gen, yr):
    request = f"""SELECT title, runtime, year, genres FROM movies 
    WHERE genres LIKE '%{gen}%' and year LIKE '%{yr}%' LIMIT 10 """
    csr.execute(request)
    films = csr.fetchall()
    return films

# select 10 movies by keyword
def select_films_by_keyword(csr, key = ''):
    request = f"""SELECT title, runtime, year, genres, plot FROM movies 
    WHERE plot LIKE '%{key}%' OR title LIKE '%{key}%' LIMIT 10"""
    csr.execute(request)
    films = csr.fetchall()
    return films

def select_actor(csr):
    csr.execute("SELECT last_name FROM actor")
    result = csr.fetchall()
    return result

def make_choise_actor_last_name(result): 
    list_act = []
    for line in result:
        list_act.append(line[0])
    return str.upper(input(f'Введите фамилию актера: {list_act}'))

# select films by actor name
def select_films_by_actor(csr,actor = ''):
    request = f"""SELECT title, runtime, year, genres FROM movies WHERE cast LIKE '%{actor}%' LIMIT 10"""
    csr.execute(request)
    films = csr.fetchall()
    return films

# select films by director name
def select_films_by_director(csr, director = ''):
    request = f"""SELECT title, runtime, year, genres FROM movies WHERE directors LIKE '%{director}%' LIMIT 10"""
    csr.execute(request)
    films = csr.fetchall()
    return films

# select hihgly rating level films by genres
def select_high_level_rating_in_genre(csr):
    request = """SELECT title, runtime, year, genres, `imdb.rating` 
            FROM movies GROUP BY genres, `imdb.rating` ORDER BY  `imdb.rating` DESC LIMIT 10"""
    csr.execute(request)
    films = csr.fetchall()
    return films

# closing DB connection
def close_connections(connection,  cursor):
    try:
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Have error : {e}")


def startDB_read():
    try: 
        connection_R = mysql.connector.connect(**dbconfig_R)
        cursor_R = connection_R.cursor()
    except Exception as e:
        print(f"Have error : {e}")
    return connection_R, cursor_R 

# conn_R, cur_R = startDB_read()
# print(select_genres(cur_R))
# print(select_years(cur_R))
# n = make_choise(select_genres(cursor_R))
#category_films_10(cursor_R, n)
#ln = make_choise_actor_last_name(select_actor(cursor_R))
#fn = make_choise_actor_first_name(select_actor_first_name(cursor_R,ln))

#print(ln, fn)
#actor_films_10(cursor,a)

#### listagg
# close_connections(connection_R, cursor_R)
