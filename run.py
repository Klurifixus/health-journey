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

return {
    'name': name,
    'email': email,    
    'nationality': nationality,
    'height': height,
    'weight': weight,
    'training_habits': training_habits,
    'steps_per_day': steps_per_day,
    'sugar_consumption': sugar_consumption,
    'fast_food_consumption': fast_food_consumption,
    'diet_balance': diet_balance,
    'water_consumption': water_consumption,
    'sleep_quality': sleep_quality
        
}

#Calculate BMI
def calculate_bmi(height, weight):
    return weight / (height ** 2)

#Generate Advice BMI:

def generate_advice(bmi):
    if bmi < 18.5:
        return "You are underweight. Consider consulting a nutritionist or a doctor."
    elif 18.5 <= bmi < 24.9:
        return "You have a normal weight. Maintain your healthy habits!"
    elif 25 <= bmi < 29.9:
        return "You are overweight. Consider adopting healthier eating habits and regular exercise."
    else:
        return "You are obese. It's important to consult a health professional."

# Generate Advice on training habits:
if data['training_habits'] == "n": 
    advice_list.append("Regular exercise can greatly improve your health. Consider starting with light exercises.")
       