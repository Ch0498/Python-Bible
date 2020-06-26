print ("                                                  COMPARER")
print ("                                                                                               by Navdeep")
num1 = input("Enter the first number :")
num2 = input("Enter the second number :")
res1 = "{} is greater than {}".format(num1,num2)
res2 = "{} is greater than {}".format(num2,num1)
if num1 > num2:
    print(res1)
elif num1 < num2:
    print(res2)
else: 
    print("Both are equal.")
l = input(" ")
