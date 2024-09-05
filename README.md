Weather App
Description
This Weather App allows users to get the current weather information for any city they search. The app provides details such as temperature, weather description, and an icon representing the weather condition. Additionally, users can learn about the Product Manager Accelerator (PM Accelerator) through an info button.

Features
City-based Weather Search: Enter any city name to retrieve and display the current weather conditions.
Weather Icon: Displays a relevant icon for the weather condition.
Temperature and Description: Shows the current temperature in Celsius and a brief description of the weather.
PM Accelerator Info: An informational popup provides details about the PM Accelerator program.
Installation and Setup
Prerequisites
Python 3.x installed on your system.
The following Python packages are required:
tkinter: For creating the GUI.
requests: To fetch weather data from the OpenWeatherMap API.
Pillow: For handling and displaying weather icons.
ttkbootstrap: For enhanced styling of the tkinter widgets.

Installation
Clone or download this repository.
Install the required packages using pip:

pip install requests Pillow ttkbootstrap


Running the App
Open your terminal or command prompt.
Navigate to the directory containing the script.
Run the script using Python:

python app.py


Usage
Enter the name of a city in the input field.
Click the "Search" button to fetch and display the weather details.
Click the "Info" button to learn more about the PM Accelerator program.

What I Did
Weather API Integration: Implemented a function get_weather() to fetch weather data from the OpenWeatherMap API.
GUI Development: Created a simple yet functional user interface using tkinter and ttkbootstrap for a modern look.
Weather Display: Parsed and displayed relevant weather information, including temperature and description.
Weather Icon: Used the Pillow library to fetch and display weather condition icons.
PM Accelerator Info: Added an info button that triggers a message box with details about the PM Accelerator program.

API Key
The app uses a free API key provided by OpenWeatherMap.
