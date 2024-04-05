#Question 2 Film Kütüphanesi Yönetim Sistemi Projesi
import json

# Function to load movie data from a file
def load_data():
    try:
        with open("movies.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:  # Handle the case where the file doesn't exist
        data = {}
    return data

# Function to save movie data to a file
def save_data(data):
    with open("movies.json", "w") as file:
        json.dump(data, file)

# Function to add a new movie to the collection   
def add_movie(movie_coll):  
    print("Enter information for the movie you want to add")
    name = input("Name of the movie: ").lower()
    director = input("Name of the director: ").lower()
    year = input("Release year: ")
    genre = input("Genre: ").lower()
    movie_coll[name] = {'director': director, 'year': year, 'genre': genre}
    print("Movie added successfully!")

# Function to edit an existing movie
def edit_movie(movie_coll):
    movie_name = input("Enter the movie name you want to edit: ").lower()
    if movie_name in movie_coll:
        field = input("Enter the field you want to edit (Director/Year/Genre): ").lower()
        if field in movie_coll[movie_name]:  
            new_data = input(f"Enter the correct {field} info: ")
            movie_coll[movie_name][field] = new_data
            print("Movie information updated successfully!")
        else:
            print("Invalid choice")
    else:
        print(f"'{movie_name.capitalize()}' not found in your collection")

# Function to delete a movie from the collection
def delete_movie(movie_coll):
    movie_name = input("Enter the name of the movie you want to delete: ").lower()
    if movie_name in movie_coll:
        del movie_coll[movie_name]
        print(movie_name, "has been deleted from your collection")
    else:
        print(f"'{movie_name.capitalize()}' not found in your collection")

# Function to display the movie collection
def display_movies(movie_coll):
    for name, info in movie_coll.items():
        print(f"Title: {name.capitalize()}    Director: {info['director'].capitalize()}    Year: {info['year']}    Genre: {info['genre'].capitalize()}")

# Function to filter and display the movie collection
def filter_movies(movie_coll):
    valid_filters = ['director', 'year', 'genre']
    filter_type = input("Enter filter type (Director/Year/Genre): ").lower()

    if filter_type not in valid_filters:
        print("Invalid filter type!")
        return
    
    filter_value = input(f"Enter {filter_type} to filter by: ")
    filtered_collection = {}
    for name, info in movie_coll.items():
        if filter_value == info[filter_type]:
            filtered_collection[name] = info

    if filtered_collection:
        display_movies(filtered_collection)
    else:
        print("No movies found with the specified filter criteria.")

# Function to filter and display the movie collection
def clear_collection(movie_coll):
    print("Are you sure you want to clear your collection? This cannot be undone!")
    confirmation = input("type 'yes' to comfirm deleting your entire collection: ")
    movie_coll.clear()
    print("Deleting...")
    print("Your movie collection is empty now")
    
# Main function to run the program
def main():
    movie_collection = load_data()  # Load movie data from file
    while True:
        print("\n1 add movie\n2 edit movie\n3 delete movie\n4 display the whole collection\n5 filter the collection\n'clear' delete whole collection\n'Q' Exit")
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
            save_data(movie_collection)  # Save movie data to file before exiting
            print("Saving...")
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()
    

    

    


    
