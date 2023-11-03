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
- [The Project Story](#the-project-story)

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
I would like to extend my gratitude to those who have contributed knowledge and advice towards the creation of this project:

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

## The Project Story
To start the story of this project, I will let you know right from the beginning that because of my personality trait of wanting to perfect my vision, I lost track of the criteria for this project. My CLI turned into a web application, and if you have time or are simply wondering why this is so basic, I will provide a link to that below. But first, let me give you my story: I spent over a week building my first project, starting with envisioning how it would look, getting the git commits just right, and creating a structure and study plan for the project. I felt calm and really enjoyed the process. However, I made one mistake; I thought I knew what was asked of me, and in the process of learning Python and everything else, I used different study platforms. I used projects on YouTube and Udemy. My plan was to learn first, then tackle the project. When I felt more confident with Python, I was too eager to start, so I just scrolled through the criteria too fast and completely missed the importance of making a CLI.

After coding for a couple of days and realizing that it was starting to work on Heroku, I sent an email to my mentor and David at the Code Institute. And I got the answer: you have built a web application and not a CLI; the templates you should have used are not there. Of course, that was because I deleted them when they didn't work with Flask. Anyway, this was 3 days ago, so I was in a bit of a hurry to create what I was supposed to do. That made me a little stressed, so my git commits suffered, and the programming was just thrown together—just to make it work and to pass the criteria. And God help me, I hope it will. In one way, I am grateful for my eagerness and mistake, because this has given me more education and knowledge. I truly feel that this education has made me confident to solve any problems I may face in the future, one way or another. And for that, I am always grateful and proud to be a Code Institute student. Because I wouldn't believe it if someone told me that I would be where I am today in coding in just a couple of weeks. And I have a long way to go, and I fucking love it!

Anyhow, here is the links of this projects missdirection
:

https://vigorous-32e31799ae7b.herokuapp.com/

https://github.com/Klurifixus/Vigorous

## Workflow chart:
![Flow Chart picture](assets/documentation/flowchart.png)
