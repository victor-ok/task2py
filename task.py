import random  
import string

def user_details():
    first_name=input("Enter your First Name :\n ")
    last_name=input("Enter your Last Name :\n ")
    user_mail=input("Enter your Email address\n ")

    details = {
        "First name" : first_name,
        "Last name" : last_name,
        "User mail" : user_mail,
    }
    return(details)


def gen_password(details):    
    characters = string.ascii_lowercase
    length = 5
    random_password = "".join(random.choice(characters)for i in range(length))
    password = str(details[0][0:2] + details[1][-2:] + random_password) 
    return password


Storage = []
Continue = True
while Continue:
    details = user_details()
    password = gen_password(details)
    print(f"Your generated password is {password}")
    confirm_password = input("Do you like the generated password? [Y/N]")
    Confirm = True

    while Confirm:
        if confirm_password == "Y":
            details.append(password)
            Storage.append(details)
            confirm =False
        else:
            user_password = str(input("Please input your desired password\n Characters must be more than 7: "))
            password_length =True
            while password_length:
                if len(user_password) >= 7:
                    print("Your password has been accepted")
                    details.append(user_password)
                    Storage.append(details)
                    password_length = False
                    Confirm = False
                else:
                    user_password = input("Your password was not accepted\n Please enter a password of more than 7 characters")

new_user =str(input("Do you want to register another user?\n Y or N: "))
if new_user =="N":
    Continue = True
    for details in Storage:
        print()
        print(f"First Name: {details[0]}")
        print(f"Last Name: {details[1]}")
        print(f"Email: {details[2]}")
        print(f"Password: {details[-1]}")
        print()
else:
    Continue = False
