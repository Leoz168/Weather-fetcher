# Weather Fetcher Application

## Description
The Weather Fetcher Application is a web application developed using Flask for the backend and HTML/CSS/JavaScript for the frontend. It retrieves real-time weather data from the OpenWeatherMap API and displays it to the user. The application includes temperature conversion functionality, allowing users to view temperatures in both Fahrenheit and Celsius. The user interface is seamless and responsive, utilizing AJAX calls to dynamically update weather data without page refreshes. The application also ensures efficient data handling and secure cross-origin resource sharing (CORS) compliance.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)
5. [Acknowledgements](#acknowledgements)
6. [Contact Information](#contact-information)

## Features
- Real-time weather data retrieval from the OpenWeatherMap API
- Secure cross-origin resource sharing (CORS) compliance
- Responsive user interface with dynamic updates using AJAX


## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Leoz168/weather-fetcher.git
   ```
2. Navigate to the project directory:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Set up the environment variables. Change the config file in the backend.
   ```py
   API_KEY=your_openweathermap_api_key
   ```
6. Run the application:
   ```
   flask run
   ```

## Usage
1. Open your web browser and go to http://127.0.0.1:5000/.
2. Enter the city name to fetch the weather data.
3. View the real-time weather data.

## Lisence
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledges
OpenWeatherMap for the weather data API.
Flask, for providing a simple and powerful web framework.

