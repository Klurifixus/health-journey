# Get user input
def get_user_input():
    name = input("Enter your name: ")
    email = None
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        else:
            print("Invalid email address. Please try again.")

nationality = input("Enter your nationality: ").capitalize()            