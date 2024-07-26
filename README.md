# AI Agent for Travel Duration

This repository contains codes for an AI agent that provides real-time travel duration information between two locations for a given mode of transportation.

The application leverages **OpenAI's Chat Completions** API for natural language processing, **Google Maps Distance Matrix API** for accurate travel duration calculation and **Flask-based web user interface** for easy interaction.

## Features
-**Natural language processing**: Uses OpenAI's gpt-4o-mini to extract information from users and generate outputs in natural language. LLM model can be changed.  
-**Real-time travel information**: Integrates with Google Maps Distance Matrix API to provide current duration based on traffic conditions.  
-**Multiple transport modes**: Supports multiple transport modes such as driving, walking, biking and transit. **Note: when valid starting and destination addresses are given, travel mode defaults to driving.**    
-**User-friendly web UI**: Provides a simple web UI for each interaction with the application.  
-**Incomplete query handling**: Identifies and handles missing information in queries.  
-**Irrelevant query handling**: Identifies and handles queries not related to travel duration.  

## Requirements

- Python 3.7+
- Flask
- Requests
- openai
- Dotenv (for environment variable management)



 
