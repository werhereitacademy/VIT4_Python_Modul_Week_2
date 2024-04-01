

print(""""
|=====Movie Library Management System======[-][o][x]
|           M O V I E   M  E  N  U                 | 
|   1- Add Movie                                   | 
|   2- Edit Movie                                  | 
|   3- Wiew Collection                             | 
|   4- Delete Movie                                | 
|   5- Exit                                        | 
|               version 1.02                       |       
|           copyright@vit4 group2                  |
|==================================================| """)
menu_choose= input("Please choose a nummer:")

def add_movie():
    movie_name= input ("Enter the Movie Name:")
    director= input("Enter the Director:")
    release_year= input("Enter the Release Year:")
    genre = input("Enter the Genre :")

    movie_dictionary= {
        "Movie": movie_name,
        "Director": director,
        "Release Year": release_year,
        "Genre": genre
        }
    print(movie_dictionary)


if menu_choose == "1" :
    add_movie()
