import gspread
from google.oauth2.service_account import Credentials
import os

# Google Sheets API setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Create a credentials object from the service account file
CREDS = Credentials.from_service_account_file('creds.json')
# Create a scoped credentials object using the defined scope
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
# Create a client for interacting with the Google Sheets API
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
# Open the specified Google Sheet
SHEET = GSPREAD_CLIENT.open("health_calculator")


def store_data_to_sheet(data):
    """
    Store the user data into the first worksheet of the Google Sheet.

    Parameters:
        data (dict): A dictionary containing the user's health data.

    Returns:
        bool: True if data was stored successfully, False otherwise.
    """
    worksheet = SHEET.get_worksheet(0)
    bmi = calculate_bmi(data['height'], data['weight'])
    data_row = [
        # Following the structure of the Google Sheet to append the row
        data['name'],
        data['email'],
        data['nationality'],
        data['height'],
        data['weight'],
        bmi,
        # Additional user health data
        data['training_habits'],
        data['steps_per_day'],
        data['sugar_consumption'],
        data['fast_food_consumption'],
        data['diet_balance'],
        data['water_consumption'],
        data['sleep_quality']
    ]

    # Append to ewcel row
    try:
        worksheet.append_row(data_row)
        return True
    except Exception as e:
        # A catch-all for any other exceptions that you didn't explicitly catch
        print(f"An unexpected error occurred: {e}")
        return False


def main():
    """
    The main function to run the Health Calculator application.
    """

    while True:  # This is the main loop until the user wants to exit
        user_data = get_user_input()
        store_data_to_sheet(user_data)
        os.system('cls' if os.name == 'nt' else 'clear')
        advice = generate_advice(user_data)
        print(advice)
        # Ask if the user wants to run the test again
        run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()
        if run_again != 'yes':
            break


def get_user_input():
    """
    Collect user input for various health metrics and validate them.

    Returns:
    dict: A dictionary containing validated user input data.
    """
    name = input("Enter your name: ")
    email = None
    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email and email.find("@") < email.rfind('.'):
            break
        else:
            print("Invalid email address. Please try again.")

    nationality = input("Enter your nationality: ").capitalize()

    # Health questions
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

    training_habits = input("Do you have any training habits?(yes/no): ").lower()

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

# Calculate BMI


def calculate_bmi(height, weight):
    """
    Calculate the Body Mass Index (BMI) based on height and weight.

    Parameters:
    height (float): Height of the user in meters.
    weight (float): Weight of the user in kilograms.

    Returns:
    float: The calculated BMI.
    """
    return weight / (height ** 2)

# Advice BMI:


def generate_advice(data):
    """
    Generate personalized health advice based on the user's health data.

    Parameters:
    data (dict): A dictionary containing the user's health data, including BMI.

    Returns:
    str: A string of health advice.
    """
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
            advice_list.append("Focus on nutrition and take walks for your health")
        elif bmi < 24.9:
            advice_list.append("Consider incorporating regular training")
        else:
            advice_list.append("Regular exercise can greatly improve your health.")

    elif data['training_habits'] == "yes":
        if bmi < 18.5:
            advice_list.append("Focus on nutrition along with exercise.")
        elif bmi < 24.9:
            advice_list.append("Great job maintaining a healthy weight!")
        else:
            advice_list.append("Consider workouts focusing on weight management.")

    # Advice on steps per day:
    if data['steps_per_day'] < 5000:
        if bmi < 18.5:
            advice_list.append("Consult a nutritionist for a balanced lifestyle.")
        elif bmi < 24.9:
            advice_list.append("Consider increasing your daily steps.")
        else:
            advice_list.append("Increase daily steps for better weight management.")

    # Advice based on sugar consumption
    if data['sugar_consumption'] in ['daily', 'weekly']:
        if bmi < 18.5:
            advice_list.append("Focus on calories from nutritious sources")
        elif bmi < 24.9:
            advice_list.append("Maintain your weight with balanced nutrition.")
        else:
            advice_list.append("Reduce your sugar intake for better overall health.")

    # Advice based on fast food consumption
    if data['fast_food_consumption'] in ['daily', 'weekly']:
        if bmi < 18.5:
            advice_list.append("Consider a healthier diet.")
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


if __name__ == "__main__":
    main()
