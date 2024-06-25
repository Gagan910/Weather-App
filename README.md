# Weather-app
# RoboSpeaker 2.1
# App Link
https://weather-app-bsj8yxzzungsmsxdzsrhmn.streamlit.app/
RoboSpeaker is a simple Python script that fetches current weather information for a specified city and speaks out the temperature using text-to-speech synthesis.

## Features

- Fetches current weather information using the WeatherAPI
- Uses pyttsx3 library for text-to-speech synthesis
- Easy to use and customize

## Installation

1. Clone the repository:

    
    git clone https://github.com/<your-username>/RoboSpeaker.git
  

2. Install the required libraries:

   
    pip install requests pyttsx3
   

## Usage

1. Run the script:

    python main.py


2. Enter the name of the city when prompted.

3. RoboSpeaker will fetch the current weather information and speak out the temperature.

## API Key

To use the WeatherAPI, you need to obtain an API key from [WeatherAPI](https://www.weatherapi.com/). Once you have the API key, replace `YOUR_API_KEY` in the `url` variable in `main.py` with your actual API key.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or feature requests, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
