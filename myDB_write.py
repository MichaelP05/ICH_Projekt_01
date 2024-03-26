import mysql.connector
# Параметри для подключения записи и чтения из таблиц журналами
dbconfig_W = {'host': '',
            'user': '',
            'password': '',
            'database': ''}


# insert record into database
def write_record(csr, conn, data):
    # "req_type": 1, "actor": "", "director": "", "genre": "", "started": year_code, "keyword": ""
    request = """INSERT INTO request_journal (req_type, actor, director, genre, started, keyword) 
             VALUES (%(req_type)s, %(actor)s, %(director)s, %(genre)s, %(started)s, %(keyword)s)"""
    try:
        csr.execute(request, data)
    except Exception as e:
        print(f"Writing error : {e}")
    conn.commit()

# select most 3 popular query
def popular_queries_3(csr):
    request = """SELECT rt.title, rj.genre, rj.started, rj.keyword, rj.director, rj.actor,
        CONCAT(rt.title, ' ', rj.genre, ' ', rj.started, ' ', rj.keyword, ' ', rj.director, ' ', rj.actor) AS d,
        COUNT(rj.req_type)
        FROM request_journal AS rj JOIN request_type AS rt ON rt.t_id = rj.req_type
        GROUP BY rt.title, rj.genre, rj.started, rj.keyword, rj.director, rj.actor
        ORDER BY COUNT(rj.req_type) DESC
        LIMIT 3"""

    try:
        csr.execute(request)
    except mysql.exception as e:
        print(f"Writing error : {e}")
    result = csr.fetchall()
    return result

# select 10 most popular type of request with parameters
def popular_seeking_parameters_10(csr):
    request = """SELECT rt.title, rj.genre, rj.started, rj.keyword, rj.director, rj.actor,
       CONCAT(rt.title, ' ', rj.genre, ' ', rj.started, ' ', rj.keyword, ' ', rj.director, ' ', rj.actor) AS d,
       COUNT(*) AS count FROM request_journal AS rj JOIN request_type AS rt ON rt.t_id = rj.req_type
        GROUP BY rt.title, rj.genre, rj.started, rj.keyword, rj.director, rj.actor, rt.title
        LIMIT 10"""
    try:
        csr.execute(request)
    except mysql.exception as e:
        print(f"Writing error : {e}")
    result = csr.fetchall()
    return result

# most popular genres in requests 
def popular_seeking_genres_5(csr):
    request = """SELECT genre, COUNT(*) AS genre_cnt FROM request_journal
                WHERE genre IS NOT NULL GROUP BY genre ORDER BY genre_cnt DESC
                LIMIT 5"""
    try:
        csr.execute(request)
    except Exception as e:
        print(f"Writing error : {e}")
    result = csr.fetchall()
    return result

# connection must be closed
def close_connections(connection,  cursor):
    try:
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Have error : {e}")


# Open journalzing database. We can made queries also.
def startDB_write():
    try:
        connection_W = mysql.connector.connect(**dbconfig_W)
        cursor_W = connection_W.cursor()
    except Exception as e:
        print(f"Have error: {e}")
    return connection_W, cursor_W

