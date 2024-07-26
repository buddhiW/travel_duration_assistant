# AI Agent for Travel Duration

This repository contains codes for an AI agent that provides real-time travel duration information between two locations for a given mode of transportation.

The application leverages **OpenAI's Chat Completions** API for natural language processing, **Google Maps Distance Matrix API** for accurate travel duration calculation and **Flask-based web user interface** for easy interaction.

## Features
- **Natural language processing**: Uses OpenAI's gpt-4o-mini to extract information from users and generate outputs in natural language. LLM model can be changed.  
- **Real-time travel information**: Integrates with Google Maps Distance Matrix API to provide current duration based on traffic conditions.  
- **Multiple transport modes**: Supports multiple transport modes such as driving, walking, biking and transit. **Note: when valid starting and destination addresses are given, and valid travel mode is not given, travel mode defaults to driving.**    
- **User-friendly web UI**: Provides a simple web UI for each interaction with the application.  
- **Incomplete query handling**: Identifies and handles missing information in queries.  
- **Irrelevant query handling**: Identifies and handles queries not related to travel duration.  

## Requirements

- Python 3.7+
- Flask
- Requests
- openai
- Dotenv (for environment variable management)

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/buddhiW/travel_duration_assistant.git
    cd travel_duration_assistant
    ```
2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```
3. **Setup API keys**

    - Obtain an API key from OpenAI.
    - Obtain an API key from Google Maps.
    - Create a `.env` file in the root directory and add the API keys:

    ```
    OPENAI_API_KEY=your_openai_api_key
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```

## Usage

1. **Run the web application**

    ```bash
    python app.py
    ```

2. **Open the web interface**

    Open your web browser and go to http://127.0.0.1:5000 to access the web UI.

## File structure

- `app.py`: Main Flask application.
- `assistant_utils.py`: All functions related to the AI assistant.
- `templates/index.html`: HTML template for the web UI.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment variables for API keys (not included in the repository).




 
