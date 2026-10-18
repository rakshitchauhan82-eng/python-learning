name='Rakshit Chauhan'
password='Say@Hy$04'
user_name=input('Enter username: ')
user_password=input('Enter password: ')

if user_name == name and user_password == password :
    print("Login successful")

elif user_name == name and user_password != password :
    print("Invalid Password!")

elif user_name != name and user_password == password :
    print("Invalid username!")

else :
    print("invalid username and password !")

