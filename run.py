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

#Height and weight in numbers 
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

#Health questions
training_habits = input("Do you have any training habits? (y/n): ").lower()
steps_per_day = int(input("How many steps do you take on average per day? "))
sugar_consuption = ("How often do you consume sugar? (daily/weekly/monthly/rarely): ").lower()
fast_food_consumption = ("How often do you consume fast food? (daily/weekly/monthly/rarely): ").lower()
diet_balance = input("Do you eat a balanced diet? (yes/no): ").lower()
water_consumption = input("Do you drink enough water? (yes/no): ").lower()
sleep_quality = input("How's your sleep quality? (good/average/poor): ").lower()


#Calculate BMI
          