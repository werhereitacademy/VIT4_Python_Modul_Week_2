# Question 2 Film Kütüphanesi Yönetim Sistemi Projesi
"""
1 add movie
2 edit movie
3 delete movie
4 display the whole collection
5 filter the collection
'clear' delete whole collection
Q Exit
"""

def main():
    movie_collection = {}
    while True:
        print(
            "\n1 add movie\n2 edit movie\n3 delete movie\n4 display the whole collection\n5 filter the collection\n'clear' delete whole collection\nQ Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_movie(movie_collection)
        elif choice == '2':
            edit_movie(movie_collection)
        elif choice == '3':
            delete_movie(movie_collection)
        elif choice == '4':
            display_movies(movie_collection)
        elif choice == '5':
            filter_movies(movie_collection)
        elif choice == 'clear':
            clear_collection(movie_collection)
        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice")


main()





def add_movie(movie_coll):
    print("Enter information for the movie you want to add")
    name = input("Name of the movie: ")
    director = input("Name of the director: ")
    year = input("Release year: ")
    genre = input("Genre: ")
    movie_coll[name] = {'Director': director, 'Year': year, 'Genre': genre}
    print("Movie added successfully")


def edit_movie(movie_coll):
    movie_name = input("Enter the movie name you want to edit: ")

    if movie_name in movie_coll:
        print("Enter,\n1 to edit movie name\n2 to edit director's name\n3 to edit release year\n4 to edit genre")
        choice = input("Enter your choice now: ")

        if choice == '1':  # Edit movie name
            new_name = input("Enter the correct version of the movie name: ")
            movie_coll[new_name.lower()] = movie_coll.pop(movie_name)

        elif choice == '2':  # Edit director's name
            new_director = input("Enter the correct version of director's name: ")
            movie_coll[movie_name]['Director'] = new_director.lower()

        elif choice == '3':  # Edit release year
            new_year = input("Enter the correct release year: ")
            movie_coll[movie_name]['Year'] = new_year

        elif choice == '4':  # Edit genre
            new_genre = input("Enter the correct genre: ")
            movie_coll[movie_name]['Genre'] = new_genre.lower()

        else:
            print("Invalid choice")
    else:
        print(f"'{movie_name}' not found in your collection")


def delete_movie(movie_coll):
    movie_name = input("Enter the name of the movie you want to delete: ")
    if movie_name in movie_coll:
        del movie_coll[movie_name]
        print(movie_name, "has been deleted from your collection")
    else:
        print(f"'{movie_name}' not found in your collection")


def display_movies(movie_coll):
    for name, info in movie_coll.items():
        print(f"Title: {name}    Director: {info['Director']}    Year: {info['Year']}    Genre: {info['Genre']}")


def filter_movies(movie_coll):
    print("Filter according to:\n1 director's name\n2 release year\n3 genre")
    choice = input("Enter your choice now: ")

    if choice == '1':
        director = input("Enter the director's name: ")
        new_collection = {}
        for name, info in movie_coll.items():
            if director == info['Director']:
                new_collection[name] = info

    elif choice == '2':
        year = input("Enter the release year: ")
        new_collection = {}
        for name, info in movie_coll.items():
            if year == info['Year']:
                new_collection[name] = info

    elif choice == '3':
        genre = input("Enter the genre: ")
        new_collection = {}
        for name, info in movie_coll.items():
            if genre == info['Genre']:
                new_collection[name] = info
    else:
        print("Invalid choice!")

    display_movies(new_collection)


def clear_collection(movie_coll):
    print("Are you sure you want to clear your collection? This cannot be undone!")
    confirmation = input("type 'yes' to comfirm deleting your entire collection: ")
    movie_coll.clear()
    print("Deleting...")
    print("Your movie collection is empty now")
