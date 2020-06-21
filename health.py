from random import randint
from time import sleep

print(health)
while True:
    health = int(input("Enter your player health :"))
    sleep(0.5)
    difficulty = int(input("Enter the difficulty of incresing the player health []:"))
    sleep(0.5)
    print("...........Generating...........")
    potion_health = int(randint(25,50))
    new_health = potion_health / difficulty
