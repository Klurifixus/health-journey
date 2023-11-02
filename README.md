# Health Calculator

The Health Calculator is a Python-based application that calculates a user's Body Mass Index (BMI) and provides personalized health advice. It utilizes Google Sheets for data storage, which facilitates the easy tracking and analysis of health metrics over time.

## Table of Contents
- [Educational Use License](#educational-use-license)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Deploying to Heroku](#deploying-to-heroku)
- [Credits](#credits)
- [Contact](#contact)
- [Constraints](#constraints)

## Educational Use License

This project was developed as a part of the Portfolio Project 3 (PP3) within the Full Stack Developer program at the Code Institute. The source code is made available strictly for educational purposes and not for commercial use.

## Prerequisites

Before starting, ensure you have the following:

- Python 3.x installed on your system
- A Google Cloud Platform account with the Sheets API enabled
- A `creds.json` file with your Google service account credentials

## Installation

To install the Health Calculator:

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/Klurifixus/health-journey.git
   ´´´

## Configurations

    1. Place your 'creds.json' file in the root directory of the project.
    2. Open the 'creds.json' file and ensure it has the necessary permissions to access Google Sheets.

## Usage

To use Health Calculator, run the following command in your terminal:
    * Run this command: python run.py

Follow the interactive prompts to input your health data. The application will calculate your BMI and output personalized health advice.    

## Features
* BMI calculation based on the user's height and weight
* Interactive collection of health and lifestyle data
* Personalized health advice tailored to the user's BMI and lifestyle inputs
* Integration with Google Sheets for robust data management

## Deploying to Heroku
This application can be deployed to Heroku. Ensure you have the Heroku CLI installed and follow these steps:

1. Log in to Heroku:
       
    * Run this command: heroku login 
    
2. Create a new Heroku app:
    
    * Run this command: heroku create

3. Push your code to Heroku:
    
    * Run this command: git push heroku main

4. Ensure that at least one instance of the app is running:
    
    * Run this command: heroku ps:scale web=1

5. Open the app in your browser:
    
    * Run this command: heroku open

## Credits
I would like to extend my gratitude to those who have contributed knowledge and advice towards the fruition of this project:

* Hurtig, a cloud engineer and a good friend, for his guidance through challenging technical scenarios.

* Annika, my partner, whose support has been unwavering, allowing me the time needed to work on this project amidst our family life.

* Sandeep, my mentor, for keeping me on track and within the scope of the project's criteria.

* David Calikes for his invaluable feedback and guidance, prompting a necessary pivot in my project's direction.

* Dr. Angela Yu and her Udemy course "100 Days of Code: The Complete Python Pro Bootcamp for 2023" for the practical exercises and different programming perspectives it offered.

* The Code Institute for their exceptional Full Stack programming course. The knowledge I've gained in a relatively short time is immense, and I am forever appreciative of the structured learning and support.

* The vast resources available on YouTube and Google, which provide an almost infinite well of information and learning opportunities.

* ChatGPT, for being a quick reference tool. Its usage, especially for troubleshooting minor issues or grammatical checks, has been indispensable.

## Contact
If you have any questions or feedback, you can contact me on my email: [pirrefixus@gmail.com](mailto:pirrefixus@gmail.com)

## Constraints
Keep in mind that the Heroku deployment terminal is set to 80 columns by 24 rows, so ensure your outputs are formatted to fit within this to prevent wrapping onto the next line.

## Contributing
- Your contributions are welcome! For significant changes, please open an issue first to discuss what you'd like to change.

## License Terms

- This project adheres to the Code Institute's stipulations for educational use. Redistribution or commercial use is not permitted.



## Creating the Heroku app

When creating your app on Heroku:
1. Add the heroku/python and heroku/nodejs buildpacks from the Settings tab in the specified order.

2. Create a Config Var named PORT and set it to '8000'.

3. If you have credentials like creds.json, create a CREDS Config Var and paste the JSON contents into the value field.

4. Connect your GitHub repository and deploy



