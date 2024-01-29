saved_name = "admin"
saved_password = "admin"

user_name = input("Enter the name: ")
user_password = input("Enter the password: ")

if (user_name == saved_name and user_password == saved_password):
    print("Welcome")
else:
    print("Locked")
    