from time import sleep

films = {
    # Marvel Cinematic Universe
    "Iron Man 1" : [13, 5],
    "Iron Man 2" : [13, 5],
    "Iron Man 3" : [13, 5],
    "Captain America: The First Avenger" : [13, 5],
    "Captain America: The Winter Soldier" : [13, 5],
    "Captian America: Civil War" : [13, 5],
    "Thor" : [13, 5],
    "Thor: Ragnorok" : [13, 5],
    "Thor: The Dark World" : [13, 5],
    "Avengers Assemble" : [13, 5],
    "Marvel's Avengers" : [13, 5],
    "Guardians of Galaxy" : [13, 5]
    "Guardians of Galaxy" : [13, 5]
    "Spiderman: Homecoming" : [13, 5],
    "Ant-Man" : [13, 5],
    "Ant-Man and The Wasp" : [13, 5],
    "Doctor Strange" : [13, 5],
    "Black-Panther" : [13, 5],
    "Captain Marvel" : [13, 5],
    "Avengers: Infinity War" : [13, 5],
    "Avengers: Endgame" : [13, 5],
    "Spiderman: Far from home" : [13, 5],
        
    # Kids Movies
    
    "Toy Story 1" : [8, 5],
    "Toy Story 2" : [8, 5],
    "Toy Story 3" : [8, 5],
    "Toy Story 4" : [8, 5],
    
    ###
    
    "The Incredibles" : [12, 5],
    "The Incredibles 2" : [12, 5],
    
    ###
    
    "Angry Birds" : [10, 5],
    "Angry Birds 2" : [10, 5]
    }

while True:

    choice = input("What film would you like to watch?: ").strip().title()
    sleep(0.5)
    if choice in films:
        age = int(input("How old are you?: ").strip())
        sleep(0.5)
        # check user age
        if age >= films[choice][0]:
            # check enough seats
            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                sleep(0.5)
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
                sleep(0.5)
        else:
            print("You are too young to see that film!")
            sleep(0.5)
    else:
        print("We don't have that film...")
        sleep(0.5)
    
