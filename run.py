import gspread
from google.oauth2.service_account import Credentials
import os

#setup the credentials for the google sheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open("health_calculator")

def store_data_to_sheet(data):
    worksheet = SHEET.get_worksheet(0)  
    bmi = calculate_bmi(data['height'], data['weight'])
    data_row = [
        data['name'],
        data['email'],
        data['nationality'],
        data['height'],
        data['weight'],
        bmi,
        data['training_habits'],
        data['steps_per_day'],
        data['sugar_consumption'],
        data['fast_food_consumption'],
        data['diet_balance'],
        data['water_consumption'],
        data['sleep_quality']
    ]
    try: 
        worksheet.append_row(data_row) 
    except Exception as e:
        print(f"An error occurred while storing data to Google-sheet: {e}")
        return False
    return True
    
def main():
    while True: #This is the main loop until the user wants to exit
        user_data = get_user_input()
        store_data_to_sheet(user_data)
        os.system('cls' if os.name == 'nt' else 'clear')
        advice = generate_advice(user_data) 
        print(advice)
        # Ask if the user wants to run the test again
        run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()
        if run_again != 'yes':
            break #  no or else, test will exit

def get_user_input():
    name = input("Enter your name: ")
    email = None
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email and email.find("@") <email.rfind('.'):
            break
        else:
            print("Invalid email address. Please try again.")

    nationality = input("Enter your nationality: ").capitalize()  
    
#Health questions
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height > 0:
                break
            else:
                print("Invalid height. Please try again.")
        except ValueError:
            print("Invalid height. Please enter your height in meters.")
            
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight > 0:
                break
            else:
                print("Invalid weight. Please try again.")
        except ValueError:
            print("Invalid weight. Please enter your weight in kilograms.")
  
    training_habits = input("Do you have any training habits? (yes/no): ").lower()

    while True:
        try:
            steps_per_day = int(input("How many steps do you take on average per day? "))
            if steps_per_day >= 0:
                break
            else:
                print("Please enter a valid number of steps.")
        except ValueError:
            print("Invalid input. Please enter an average number of steps per day.")
    
    # Validate sugar consumption input
    while True:
        sugar_consumption = input("How often do you consume sugar? (daily/weekly/monthly/rarely): ").lower()
        if sugar_consumption in ['daily', 'weekly', 'monthly', 'rarely']:
            break
        else:
            print("Invalid choice. Please select from daily, weekly, monthly, or rarely.")

    # Validate fast food consumption input
    while True:
        fast_food_consumption = input("How often do you consume fast food? (daily/weekly/monthly/rarely): ").lower()
        if fast_food_consumption in ['daily', 'weekly', 'monthly', 'rarely']:
            break
        else:
            print("Invalid choice. Please select from daily, weekly, monthly, or rarely.")

    # Validate diet balance input
    while True:
        diet_balance = input("Do you eat a balanced diet? (yes/no): ").lower()
        if diet_balance in ['yes', 'no']:
            break
        else:
            print("Invalid choice. Please select either 'yes' or 'no'.")

    # Validate water consumption input
    while True:
        water_consumption = input("Do you drink enough water? (yes/no): ").lower()
        if water_consumption in ['yes', 'no']:
            break
        else:
            print("Invalid choice. Please select either 'yes' or 'no'.")

    # Validate sleep quality input
    while True:
        sleep_quality = input("How's your sleep quality? (good/average/poor): ").lower()
        if sleep_quality in ['good', 'average', 'poor']:
            break
        else:
            print("Invalid choice. Please select from good, average, or poor.")

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

# Advice BMI:

def generate_advice(data):
    bmi = calculate_bmi(data['height'], data['weight'])
    advice_list = []

    advice_list.append(f"Your BMI is {bmi:.1f}.\n")

    # Determine BMI category
    if bmi < 18.5:
        advice_list.append("This is considered underweight.")
    elif 18.5 <= bmi < 24.9:
        advice_list.append("This is considered a normal weight.")
    elif 25 <= bmi < 29.9:
        advice_list.append("This is considered overweight.")
    else:
        advice_list.append("This is considered obese.")

    advice_list.append("\nHere are some pieces of advice you should consider:\n")

    # Advice on training habits:
    if data['training_habits'] == "no":
        if bmi < 18.5:
            advice_list.append("Consider focusing on nutrition and consulting a nutritionist. Light exercises might also be beneficial.")
        elif bmi < 24.9:
            advice_list.append("Consider incorporating regular, light exercises into your routine.")
        else:
            advice_list.append("Regular exercise can greatly improve your health. Consider starting with light exercises.")

    elif data['training_habits'] == "yes":
        if bmi < 18.5:
            advice_list.append("Focus on nutrition along with exercise. Consider consulting a nutritionist.")
        elif bmi < 24.9:
            advice_list.append("Great job maintaining a healthy weight with an active lifestyle!")
        else:
            advice_list.append("Keep up the good work! Consider workouts focusing on weight management.")

    # Advice on steps per day:
    if data['steps_per_day'] < 5000:
        if bmi < 18.5:
            advice_list.append("Consider increasing steps and focusing on nutrition. Consult a nutritionist for a balanced diet.")
        elif bmi < 24.9:
            advice_list.append("Consider increasing your daily steps for enhanced cardiovascular health.")
        else:
            advice_list.append("Increase daily steps for better weight management. Set daily goals for motivation.")

    # Advice based on sugar consumption
    if data['sugar_consumption'] in ['daily', 'weekly']:
        if bmi < 18.5:
            advice_list.append("Focus on calories from nutritious sources, moderate sugar intake for balanced nutrition.")
        elif bmi < 24.9:
            advice_list.append("Maintain your weight with balanced nutrition. Consider reducing sugar intake.")
        else:
            advice_list.append("Consider reducing sugar intake for better weight management and overall health.")

    # Advice based on fast food consumption
    if data['fast_food_consumption'] in ['daily', 'weekly']:
        if bmi < 18.5:
            advice_list.append("Fast food may not offer the best nutrition. Consider a healthier diet.")
        elif bmi < 24.9:
            advice_list.append("Consider reducing fast food for a more balanced diet.")
        else:
            advice_list.append("Reducing fast food can benefit weight management.")

    # Advice based on diet balance
    if data['diet_balance'] == "no":
        if bmi < 18.5:
            advice_list.append("Consider a balanced diet and consulting a nutritionist.")
        elif bmi < 24.9:
            advice_list.append("Aim for a more balanced diet.")
        else:
            advice_list.append("Focus on a balanced diet for better health.")

    # Advice based on water consumption
    if data['water_consumption'] == "no":
        advice_list.append("Ensure you're consuming enough water daily.")

    # Advice based on sleep quality
    if data['sleep_quality'] == "poor":
        advice_list.append("Improving sleep quality can benefit your overall health.")

    return '\n'.join(advice_list)

if __name__ == '__main__':
    main()     