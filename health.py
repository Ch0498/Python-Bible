from random import randint
from time import sleep

while True:
    health = int(input("Enter your player health :"))
    sleep(0.5)
    difficulty = int(input("Enter the difficulty of incresing the player health [1, 2, 3]:"))
    sleep(0.5)
    print("...........Generating...........")
    potion_health = randint(25,50)
    new_health = potion_health / difficulty
    new_health = int(new_health)
    
    final_health = new_health + health
    
    print("Player Health = {}".format(final_health))
