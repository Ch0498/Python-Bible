from time import sleep

while True:
    num1 = input("Enter the first number :")
    sleep(0.5)
    num2 = input("Enter the second number :")
    res1 = "{} is greater than {}".format(num1,num2)
    res2 = "{} is greater than {}".format(num2,num1)
    if num1 > num2:
        print(res1)
        sleep(0.5)
    elif num1 < num2:
        print(res2)
        sleep(0.5)
    else: 
        print("Both are equal.")
        sleep(0.5)
