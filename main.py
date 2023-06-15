# Define the available movie ratings and their corresponding movies
movies = {
    "G": [
        "Finding Nemo",
        "Toy Story",
        "The Lion King",
        "Coco",
        "Moana"
    ],
    "PG": [
        "The Incredibles",
        "Up",
        "Zootopia",
        "Frozen",
        "Inside Out"
    ],
    "M": [
        "The Avengers",
        "The Dark Knight",
        "Inception",
        "Interstellar",
        "Gladiator"
    ],
    "MA15+": [
        "Fight Club",
        "Pulp Fiction",
        "The Departed",
        "The Matrix",
        "Black Swan"
    ],
    "R": [
        "Scarface",
        "Goodfellas",
        "Reservoir Dogs",
        "The Godfather",
        "Taxi Driver"
    ]
}

# Define the available snacks
snacks = [
    "Popcorn",
    "Nachos",
    "Candy",
    "Ice cream",
    "Soda"
]

# Define the chatbot
def movie_chatbot():
    print("Welcome to the Movie Selector Chatbot!")
    print("I can help you select a movie to watch and suggest snacks.")
    print("Please answer the following questions.")

    while True:
        rating = input("What movie rating do you prefer? (G/PG/M/MA15+/R): ")

        if rating in movies:
            print(f"Here are some movie choices for rating '{rating}':")
            for index, movie in enumerate(movies[rating], start=1):
                print(f"{index}. {movie}")

            choice = input("Enter the number of the movie you want to watch: ")
            choice = int(choice) - 1

            if choice >= 0 and choice < len(movies[rating]):
                movie = movies[rating][choice]
                print(f"You selected '{movie}'. Enjoy!")

                print("Here are some snack choices:")
                for index, snack in enumerate(snacks, start=1):
                    print(f"{index}. {snack}")

                snack_choice = input("Enter the number of the snack you want: ")
                snack_choice = int(snack_choice) - 1

                if snack_choice >= 0 and snack_choice < len(snacks):
                    snack = snacks[snack_choice]
                    print(f"You selected '{snack}'. Enjoy your movie with {snack}!")
                else:
                    print("Invalid snack choice. Enjoy your movie!")

            else:
                print("Invalid movie choice. Please try again.")

        else:
            print("Invalid movie rating. Please try again.")

        user_input = input("Would you like another movie recommendation? (yes/no): ")

        if user_input.lower() != "yes":
            break

    print("Thank you for using the Movie Selector Chatbot. Enjoy your movie!")

# Run the chatbot
movie_chatbot()
