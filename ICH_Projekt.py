import os
import myDB_read
import myDB_write
 
def make_choise(param): 
    list_cat = []
    print('List of values in a kategory : ')
    for line in range(len(param)):
        list_cat.append(line+1)
        print(line+1,'.',param[line])
    ex = True

    while ex:
        num = int(input(f'Enter the appropriate category number: {list_cat}'))-1
        if num in range(len(param)):
            ex = False
    return param[num]

def waiting_key():
    ch = ''
    while ch == '':
        ch = input('Input  Y/y to continue....')
        if ch == 'Y' or ch == 'y':
            pass
        else:
            ch = ''

def main():
    print("Application started.")
    connR, curR = myDB_read.startDB_read()
    connW, curW = myDB_write.startDB_write()
    # show_text_Main_menu(connR, curR,connW, curW)
    try:
        show_text_Main_menu(connR, curR,connW, curW)
    except Exception as e:
        print(f"Having error main()! {e}")
        return
       
    
def show_text_Main_menu(connR, curR, connW, curW):
    M_Menu = True
    while M_Menu:
        os.system('cls')
        print("\t\tApplication menu: \n")
        print("1. Seek by year.")
        print("2. Seek by genre.")
        print("3. Seek by year and genre.")
        print("4. Seek by actor's name.")
        print("5. Seek by director's name.")
        print("6. Seek by keyword.")
        print("7. Highly imdb ratings film.")
        print("8. Most popular query.")
        print("9. Most popular query and parameters.")
        print("10. Quit.")
        choice = int(input("Please, input number : "))
        if choice == 1:
            # получаем список годов
            years = myDB_read.select_years(curR)
            # получаем код года
            year_code = make_choise(years)
            film_list = myDB_read.select_by_year_10(curR, year_code)
            t_name = f"\t\t10 MOVIES FROM {year_code}\n"
            output_list_results(film_list,t_name)
            waiting_key()
            try:
                parameters = {"req_type": 1, "actor": "", "director": "", "genre": "", "started": year_code, "keyword": ""}
                myDB_write.write_record(curW, connW, parameters)
            except Exception as e:
                print(f'Have error. Menu 1 {e}')
         
        elif choice == 2:
            # получаем список жанров
            genres = myDB_read.select_genres(curR)
            # получаем код жанра
            genre_code = make_choise(genres)
            # получаем названме жанра и запрашиваем набор фильмов
            film_list = myDB_read.select_films_genres_10(curR, genre_code)
            t_name = f"\t\t10 MOVIES {genre_code}\n"
            output_list_results(film_list, t_name)
            waiting_key()
            try:
                parameters = {"req_type": 2,"actor": "","director": "","genre": "","started": 0,"keyword": ""}
                myDB_write.write_record(curW,connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
            
        elif choice == 3:
            # получаем список годов
            years = myDB_read.select_years(curR)
            # получаем код года
            year_code = make_choise(years)
            # получаем список жанров
            genres = myDB_read.select_genres(curR)
            # получаем код жанра
            genre_code = make_choise(genres)
            # получаем названме жанра и запрашиваем набор фильмов
            film_list = myDB_read.select_films_genres_and_year_10(curR, genre_code, year_code)
            t_name = f"\t\t10 MOVIES {genre_code} FROM {year_code}\n"
            output_list_results(film_list, t_name)
            try:
                parameters = {"req_type": 3,"actor": "","director": "","genre": genre_code,"started": year_code,"keyword": ""}
                myDB_write.write_record(curW,connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
            waiting_key()
            
        elif choice == 4:
            actor = input("Please, typing actor's last name : ")
            film_list = myDB_read.select_films_by_actor(curR, actor)
            t_name = f"\t\t10 MOVIES WITH ACTOR's NAME {actor}\n"
            output_list_results(film_list, t_name)
            try:
                parameters = {"req_type": 4, "actor": actor, "director": "", "genre": "", "started": 0, "keyword": ""}
                myDB_write.write_record(curW, connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
            
            waiting_key()
            
        elif choice == 5:
            director = input("Please, typing director's last name : ")
            film_list = myDB_read.select_films_by_director(curR, director)
            t_name = f"\t\t10 MOVIES WITH DIRECTOR's NAME {director}\n"
            output_list_results(film_list, t_name)
            try:
                parameters = {"req_type": 5,"actor": actor, "director": "","genre": "","started": 0,"keyword": ""}
                myDB_write.write_record(curW,connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
            
            waiting_key()
            
        elif choice == 6:
            keyword = input("Please, typing keyword for query: ")
            film_list = myDB_read.select_films_by_keyword(curR, keyword)
            t_name = f"\t\t10 MOVIES BY KEYWORD {keyword}\n"
            output_list_results_enhanched(film_list, t_name)
            try:
                parameters = {"req_type": 6,"actor": "","director": "","genre": "","started": 0,"keyword": keyword}
                myDB_write.write_record(curW, connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
            waiting_key()            
            
        elif choice == 7:
            film_list = myDB_read.select_high_level_rating_in_genre(curR)
            t_name = f"\t\t10 MOVIES WITH HIGHLY LEVEL OF RATING \n"
            output_list_results_extended(film_list, t_name)
            try:
                parameters = {"req_type": 7,"actor": "","director": "","genre": "","started": 0,"keyword": ""}
                myDB_write.write_record(curW, connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
            waiting_key()            

            
        elif choice == 8:
            query_list = myDB_write.popular_queries_3(curW)
            t_name = f"\t\t3 MOST POPULAR TYPE OF QUERIES.\n"
            output_query_results(query_list, t_name)
            waiting_key()
            try:
                parameters = {"req_type": 8,"actor": "","director": "","genre": "","started": 0,"keyword": ""}
                myDB_write.write_record(curW,connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
            
        elif choice == 9:
            t_name = f"\t\t10 MOST POPULAR TYPE OF QUERIES AND PARAMETERS.\n"
            query_list = myDB_write.popular_seeking_parameters_10(curW)
            output_query_results(query_list, t_name)
            waiting_key()
            try:
                parameters = {"req_type": 9,"actor": "","director": "","genre": "","started": 0,"keyword": ""}
                myDB_write.write_record(curW,connW, parameters)
            except Exception as e:
                print(f'Have error menu 2 {e}')
             
        elif choice == 10: 
            close_application(connR, curR,connW, curW)
            M_Menu = False
        else:
            print('Wrong input! Try again!')
    

# Output definitions for list of the movies 
def output_list_results(movies_data, table_name=""):
    os.system('cls')
    print(table_name+"\t")
    
    print("{:<25} {:<10} {:<10} {:<30}".format("Title", "Rating", "Year", "Genres"))
    print("-" * 80)  # Line separator

    # Print movie data
    for movie in movies_data:
        title, rating, year, genres = movie
        genres_str = ', '.join(genres)
        print("{:<25} {:<10} {:<10} {:<30}".format(title, rating, year, genres_str))
    print("-" * 80)  # Line separator

# Output definitions for list of the movies with plot line and highligting
def output_list_results_enhanched(movies_data, table_name=""):
    os.system('cls')
    print(table_name+"\t")
    
    print("{:<25} {:<10} {:<10} {:<30}{:<40}".format("Title", "Rating", "Year", "Genres","Plot"))
    print("-" * 145)  # Line separator

    # Print movie data
    for movie in movies_data:
        title, rating, year, genres, plot = movie
        genres_str = ', '.join(genres)
        print("{:<25} {:<10} {:<10} {:<30}{:<40}".format(title, rating, year, genres_str, plot))
    print("-" * 145)  # Line separator

# Output definitions for list of the movies with highly rating
def output_list_results_extended(movies_data, table_name=""):
    os.system('cls')
    print(table_name+"\t")
    
    print("{:<60} {:<10} {:<10} {:<30}{:<10}".format("Title", "Rating", "Year", "Genres", "IMDB"))
    print("-" * 120)  # Line separator

    # Print movie data
    for movie in movies_data:
        title, rating, year, genres, irating = movie
        genres_str = ', '.join(genres)
        print("{:<60} {:<10} {:<10} {:<30}{:<10}".format(title, rating, year, genres_str, irating))
    print("-" * 120)  # Line separator


# Output definition for list of queries
def output_query_results(queries_data, table_name=""):
    os.system('cls')
    print(table_name+"\t")
    # Print table header
    print("{:<15} {:<15} {:<10} {:<15} {:<15} {:<15} {:<20} {:<12}".format(
        "Type", "Genre", "Year", "Keyword", "Director", "Actor", "Summary", "Count"))

    print("-" * 120)  # Line separator
    # Iterate through the movie data
    for entry in queries_data:
        # Unpack the entry
        data_type, genre, year, keyword, director, actor, title, count = entry
        
        # Print formatted movie information
        print("{:<15} {:<15} {:<10} {:<15} {:<15} {:<15} {:<15} {:<10}".format(
            data_type, genre, year, keyword, director, actor, title, count))

    print("-" * 120)  # Line separator

    
def close_application(connR, curR,connW, curW):
    myDB_read.close_connections(connR, curR)
    myDB_write.close_connections(connW, curW)
    print("Application closed.")


# Start application 
main()
