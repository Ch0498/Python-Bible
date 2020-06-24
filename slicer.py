from time import sleep

while True:
    
    email = input("What is your email address?: ").strip()
    sleep(0.5)
    # slice out user name
    user = email[:email.index("@")]
    sleep(0.5)
    # slice domain name
    domain = email[email.index("@") + 1 :]
    sleep(0.5)
    # format message
    output = "Your username is {} and your domain name is {}".format(user, domain)
    # display output message 
    print(output)
