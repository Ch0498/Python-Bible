films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters":[12, 5]
    "Iron Man 1" : [13, 5]
    "Iron Man 2" : [13, 5]
    "Iron Man 3" : [13, 5]
    "Captain America, The First Avenger"
    "Captain America, The Winter Soldier"
    "Captian America, Civil War"
    "Thor"
    "Thor Ragnorok"
    ""
    "Avengers"
    "Marvel's Avengers"
    
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
    
