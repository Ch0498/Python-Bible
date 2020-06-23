films = {
    # Marvel
    ""Iron Man 1"" : [13, 5]
    ""Iron Man 2"" : [13, 5]
    ""Iron Man 3"" : [13, 5]
    ""Captain America: The First Avenger"" : [13, 5]
    ""Captain America: The Winter Soldier"" : [13, 5]
    ""Captian America: Civil War"" : [13, 5]
    ""Thor"" : [13, 5]
    ""Thor: Ragnorok"" : [13, 5]
    ""Thor: The Dark World"" : [13, 5]
    ""Avengers Assemble"" : [13, 5]
    ""Marvel's Avengers"" : [13, 5]
    ""Spiderman: Homecoming"" : [13, 5]
    ""Ant-Man"" : [13, 5]
    ""Ant-Man and The Wasp"" : [13, 5]
    ""Doctor Strange"" : [13, 5]
    ""Black-Panther"" : [13, 5]
    ""Captain Marvel"" : [13, 5]
    ""Avengers: Infinity War"" : [13, 5]
    ""Avengers: Endgame"" : [13, 5]
    ""Spiderman: Far from home"" : [13, 5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())

        # check user age

        if age >= films[choice][0]:
            # check enough seats
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")
        
