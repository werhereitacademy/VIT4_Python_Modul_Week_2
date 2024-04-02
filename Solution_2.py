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


movie_collection={}


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

    movie_collection[movie_name]= movie_dictionary
    print(f"({movie_name}) added to the collection")

def edit_movie (movie_name):
    if movie_name in movie_collection:
        print(f"Editing {movie_name}...")
        new_data = {}
        new_data['Movie']= input(f"Enter a new movie({ movie_collection[movie_name]['Movie']}):")
        new_data['Director']= input(f"Enter a New Director ({movie_collection[movie_name]['Director']}):")
        new_data['Release Year']= input(f"Enter a New Release Year ({movie_collection[movie_name]['Release Year']}):")
        new_data['Genre']= input(f"Enter a New Genre ({movie_collection[movie_name]['Genre']}):")

        movie_collection[movie_name]= new_data
        print(f"({new_data}) uptaded")
    else:
        print(f"({movie_name}) not found in the collection.")

def view_collection():
    print("\nMovie Collection:")
    for movie_name, data in movie_collection.items():
        print(f"Movie Name: {data['Movie']}")
        print(f"Director: {data['Director']}")
        print(f"Release Year: {data['Release Year']}")
        print(f"Genre: {data['Genre']}")
        print("-" * 30)

def delete_movie (movie_name):
    if movie_name in movie_collection:
        del movie_collection[movie_name]
        print(f"{movie_name} deleted from the collection.")
    else:
        print(f"{movie_name} not found in the collection.")

import json


def save_data(filename):
    with open(filename, 'w') as file:
        json.dump(movie_collection, file)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def main():
    global movie_collection
    movie_collection = load_data('movie_data.json')

    while True:
        menu_choose = input("Please choose a number: ")
        print('=' * 51)

        if menu_choose == "1":
            add_movie()
            print('=' * 51)

        elif menu_choose == "2":
            movie_name = input("Enter the film name to edit: ")
            edit_movie(movie_name)
            print('=' * 51)

        elif menu_choose == "3":
            view_collection()
            print('=' * 51)

        elif menu_choose == "4":
            movie_name = input("Enter the Movie name to delete: ")
            delete_movie(movie_name)
            print('=' * 51)

        elif menu_choose == "5":
            save_data('movie_data.json')
            print("Exiting the program")
            print('=' * 51)
            break

        else:
            print("Invalid option! Please try again.")
            print('=' * 51)

if __name__ == "__main__":
    main()