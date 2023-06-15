def movie_chatbot():
    print("Welcome to the Movie Selector Chatbot!")
    print("I can help you select a movie to watch and suggest snacks.")
    print("Please answer the following questions.")
    while True:
        rating = input("What movie rating do you prefer? (G/PG/M/MA15+/R): ")

        if rating == "G":
            print(f"Here are some movie choices for rating G:")
            print(f"""1. finding nemo
2. toy story 
3. the lion king 
4. coco
5. moana""")

            movie = input("Enter the number of the movie you want to watch: ")
            if movie == "1":
                print(f"You selected 'finding nemo'. Enjoy!")
                
            elif movie == "2":
                print(f"You selected 'toy story'. Enjoy!")
                
            elif movie == "3":
                print(f"You selected 'the lion king'. Enjoy!")
                
            elif movie == "4":
                print(f"You selected 'coco'. Enjoy!")
                
            elif movie == "5":
                print(f"You selected 'moana'. Enjoy!")
                
        if rating == "PG":
            print(f"Here are some movie choices for rating PG:")
            print(f"""1. the incredibles
2. up
3. zootopia
4. frozen
5. inside out""")

            movie = input("Enter the number of the movie you want to watch: ")
            if movie == "1":
                print(f"You selected 'the incredibles'. Enjoy!")
                
            elif movie == "2":
                print(f"You selected 'up'. Enjoy!")
                
            elif movie == "3":
                print(f"You selected 'zootopia'. Enjoy!")
                
            elif movie == "4":
                print(f"You selected 'frozen'. Enjoy!")
                
            elif movie == "5":
                print(f"You selected 'inside out'. Enjoy!")
            
        if rating == "M":
            print(f"Here are some movie choices for rating M:")
            print(f"""1. The Avengers
2. the dark knight
3. Inception
4. interstellar
5. gladiator""")

            movie = input("Enter the number of the movie you want to watch: ")
            if movie == "1":
                print(f"You selected 'The Avengers'. Enjoy!")
                
            elif movie == "2":
                print(f"You selected 'the dark knight'. Enjoy!")
                
            elif movie == "3":
                print(f"You selected 'inception'. Enjoy!")
                
            elif movie == "4":
                print(f"You selected 'interstellar'. Enjoy!")
                
            elif movie == "5":
                print(f"You selected 'gladiator'. Enjoy!")
                
        if rating == "MA15+":
            print(f"Here are some movie choices for rating MA15+:")
            print(f"""1. Fight club
2. pulp Fiction
3. The Departed
4. The Matrix
5. Black swan""")

            movie = input("Enter the number of the movie you want to watch: ")
            if movie == "1":
                print(f"You selected 'Fight club'. Enjoy!")
                
            elif movie == "2":
                print(f"You selected 'pulp fiction'. Enjoy!")
                
            elif movie == "3":
                print(f"You selected 'the Departed'. Enjoy!")
                
            elif movie == "4":
                print(f"You selected 'The Matrix'. Enjoy!")
                
            elif movie == "5":
                print(f"You selected 'black Swan'. Enjoy!")
                
        if rating == "R":
            print(f"Here are some movie choices for rating R:")
            print(f"""1. Scarface
2. Goodfellas
3. Reservoir Dogs
4. The godfather
5. taxi driver""")

            movie = input("Enter the number of the movie you want to watch: ")
            if movie == "1":
                print(f"You selected 'Scarface'. Enjoy!")
                
            elif movie == "2":
                print(f"You selected 'goodfellas'. Enjoy!")
                
            elif movie == "3":
                print(f"You selected 'reservoir Dogs'. Enjoy!")
                
            elif movie == "4":
                print(f"You selected 'the godfather'. Enjoy!")
                
            elif movie == "5":
                print(f"You selected 'taxi driver'. Enjoy!")
        
        Snack()
        print("Thank you for using the Movie Selector Chatbot. Enjoy your movie!")
        exit()
        
        
def Snack():
    snack = input(f"""Here are the snack choices: 
1. popcorn
2. Nachos
3. Candy
4. ice cream
5. Soda. 
Enter the number of the snack you want to eat: """)
    if snack == "1":
        print("You selected popcorn as your snack. Enjoy!")
    
    if snack == "2":
        print("You selected nachos as your snack. Enjoy!")
        
    if snack == "3":
        print("You selected candy as your snack. Enjoy!")
        
    if snack == "4":
        print("You selected ice cream as your snack. Enjoy!")
    
    if snack == "5":
        print("You selected soda as your snack. Enjoy!")

    

# Run the chatbot
movie_chatbot()