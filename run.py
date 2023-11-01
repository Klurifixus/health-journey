import gspread
from google.oauth2.service_account import Credentials

#setup the credentials for the google sheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('healthdata.json')
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
    user_data = get_user_input()
    store_data_to_sheet(user_data)
    advice = generate_advice(user_data) #just displayng the advices
    print(advice)

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

    if bmi < 18.5:
        advice = "You are underweight. Consider consulting a nutritionist or a doctor."
    elif 18.5 <= bmi < 24.9:
        advice = "You have a normal weight. Maintain your healthy habits!"
    elif 25 <= bmi < 29.9:
        advice = "You are overweight. Consider adopting healthier eating habits and regular exercise."
    else:
        advice = "You are obese. It's important to consult a health professional."
        
    # Advice on training habits:
    if data['training_habits'] == "no":
        if bmi < 18.5:
            advice_list.append("Being underweight can be a concern. Focus on nutrition to ensure you're getting enough calories and nutrients. Consider consulting a nutritionist and starting with light exercises.")
        elif bmi < 24.9:
            advice_list.append("Regular exercise can benefit everyone, even if you're at a normal weight. Consider starting with light exercises.")
        else:
            advice_list.append("Given your BMI, regular exercise can greatly improve your health. Consider starting with light exercises.")
    elif data['training_habits'] == "yes":
        if bmi < 18.5:
            advice_list.append("While exercise is great, your BMI indicates you might be underweight. It's essential to focus on nutrition to ensure you're getting enough calories and a balanced intake of nutrients. Consulting a nutritionist can be beneficial.")
        elif bmi < 24.9:
            advice_list.append("Awesome! Your active lifestyle is likely helping you maintain a healthy weight. Keep it up!")
        else:
            advice_list.append("Great job on keeping active! As you continue, consider workouts that focus on weight management.")

    # Advice on steps per day:
    if data['steps_per_day'] < 5000:
        if bmi < 18.5:
            advice_list.append("While increasing your steps can be beneficial for overall health, it's crucial to focus on nutrition if you choose to be more active. Given your BMI, ensure that you're consuming enough calories and nutrients. Consider consulting a nutritionist to maintain a balanced diet as you increase your physical activity.")
        elif bmi < 24.9:
            advice_list.append("Your step count is on the lower side, even though your BMI is in a healthy range. Aim to increase your daily steps for better cardiovascular health and energy levels.")
        else:
            advice_list.append("Given your BMI, increasing your step count can be beneficial for weight management. Consider setting a daily goal to motivate yourself.")

    # Advice based on sugar consumption
    if data['sugar_consumption'] in ['daily', 'weekly']:
        if bmi < 18.5:
            advice_list.append("Even though you might be tempted to consume more sugars for calories, it's essential to ensure you're getting those calories from nutritious sources. Excessive sugar intake can lead to various health issues in the long term. Focus on balanced nutrition.")
        elif bmi < 24.9:
            advice_list.append("Maintaining a healthy weight is great! However, high sugar intake can still pose risks to your overall health. Consider moderating your sugar consumption.")
        else:
            advice_list.append("High sugar intake can lead to various health issues, including exacerbating weight-related concerns. Reducing your sugar consumption can be beneficial for weight management and overall health.")

    # Advice based on fast food consumption
    if data['fast_food_consumption'] in ['daily', 'weekly']:
        if bmi < 18.5:
            advice_list.append("While you might see fast food as an easy source of calories given your BMI, it's crucial to ensure you're nourishing your body with quality nutrients. Regular fast food might not offer the best nutrition. Focus on more wholesome and balanced meals for better health.")
        elif bmi < 24.9:
            advice_list.append("Even if your weight is in a healthy range, frequent fast food can still impact your overall health negatively. It's good to indulge occasionally, but consider incorporating more balanced meals into your diet.")
        else:
            advice_list.append("High fast food intake can contribute to weight and related health issues. Reducing your fast food consumption can be beneficial for weight management and overall health.")

    # Advice based on diet balance
    if data['diet_balance'] == "no":
        if bmi < 18.5:
            advice_list.append("Your BMI indicates you might be underweight. A balanced diet is crucial not only for weight but also for overall health. Ensure you're consuming a variety of nutrients and consider consulting a nutritionist to guide you.")
        elif bmi < 24.9:
            advice_list.append("Even if your weight is in a healthy range, not having a balanced diet can lead to nutritional deficiencies and other health issues. Aim to include a variety of foods in your meals.")
        else:
            advice_list.append("Your BMI suggests that focusing on a balanced diet could be beneficial for weight management and overall well-being. Incorporating various nutrients can help you feel better and manage your weight.")

    # Advice based on water consumption
    if data['water_consumption'] == "no":
        if bmi < 18.5:
            advice_list.append("Your BMI suggests you might be underweight. Proper hydration is essential for metabolism and overall health. Ensure you're drinking enough water daily, especially if you decide to increase your caloric intake or physical activity.")
        elif bmi < 24.9:
            advice_list.append("Even if your weight is in a healthy range, staying hydrated is crucial for bodily functions and maintaining energy levels. Aim to drink at least 8 glasses of water daily.")
        else:
            advice_list.append("Proper hydration can help with weight management and overall health. Drinking enough water can aid in digestion and help you feel full. Aim to consistently hydrate throughout the day.")

    # Advice based on sleep quality
    if data['sleep_quality'] == "poor":
        if bmi < 18.5:
            advice_list.append("Your BMI suggests you might be underweight, and poor sleep can further affect your health and metabolism. It's essential to address any sleep issues and consider consulting a health professional for guidance.")
        elif bmi < 24.9:
            advice_list.append("Even if your weight is in a healthy range, poor sleep can impact your energy levels, mood, and overall health. Prioritize good sleep hygiene and consider seeking guidance if sleep issues persist.")
        else:
            advice_list.append("Your BMI and poor sleep quality can together impact your health significantly. Improving sleep can aid in weight management and overall well-being. It's important to consult a health professional.")

    return ' '.join(advice_list)

if __name__ == '__main__':
    main()     