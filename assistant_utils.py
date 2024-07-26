from openai import OpenAI
import openai
import requests
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def get_user_input(user_query):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that processes user queries about current travel duration between two locations for a given mode of transportation"},
        {"role": "user", "content": f"Extract origin location, destination location and mode of travel from this query: {user_query}. Return None for missing values.\
                                        If the query is unrelated to travel duration, return 'OutOfContext'."}
        ]
    )

    return completion.choices[0].message.content.strip()

def parse_user_input(user_query):

    user_input = get_user_input(user_query)

    if user_input == 'OutOfContext':
        return user_input

    data = user_input.split('\n')
    origin = data[0].split(':')[1].strip()
    destination = data[1].split(':')[1].strip()
    mode = data[2].split(':')[1].strip()

    return origin, destination, mode

def get_travel_duration(origin, destination, mode):
    
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "mode": mode,
        "key": api_key
    }

    response = requests.get(url, params=params).json()

    error_messages = []
    if not response['destination_addresses'][0]:
        error_messages.append('Please provide valid destination address.')

    if not response['origin_addresses'][0]:
        error_messages.append('Please provide valid starting address.')

    if mode == 'None':
        error_messages.append('Please provide valid mode of transportation')

    if response['status'] == 'OK' and response['rows'][0]['elements'][0]['status'] == 'OK':
        duration = response['rows'][0]['elements'][0]['duration']['text']
        return duration, error_messages
    #else:
    #    return None

    return None, error_messages

def generate_output(origin, destination, mode, duration):

    # if origin == 'None' or destination == 'None' or mode == 'None':
    #     prompt = f"Mention to the user the None values out of {origin}, {destination} and {mode}."
    # else:
    #     prompt = f"Combine following information into a response: Origin location: {origin}, destination location: {destination}, travel mode:{mode} and duration: {duration}."
    
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that combines given four inputs into a short, clear, to the point natural language output"},
        {"role": "user", "content": f"Combine following information into a response: Origin location: {origin}, destination location: {destination}, travel mode:{mode} and duration: {duration}."} ### If any origin location or destination location or travel mode are None, mention this to the user. Do not mention duration in this case. update this to hanndle edge cases
        ]
    )
    return completion.choices[0].message.content

def generate_output_error(error_messages):

    # if origin == 'None' or destination == 'None' or mode == 'None':
    #     prompt = f"Mention to the user the None values out of {origin}, {destination} and {mode}."
    # else:
    #     prompt = f"Combine following information into a response: Origin location: {origin}, destination location: {destination}, travel mode:{mode} and duration: {duration}."
    
    prompt = f"Combine the given error messages: {error_messages} into a clear and concise error message"

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that lets the user know about invalid inputs."},
        {"role": "user", "content": prompt} ### If any origin location or destination location or travel mode are None, mention this to the user. Do not mention duration in this case. update this to hanndle edge cases
        ]
    )
    return completion.choices[0].message.content


def run_assistant(user_query):

    user_input = parse_user_input(user_query)

    if user_input == 'OutOfContext':
        return "I'm sorry, I did not understand your question. Please input a query related to travel duration calculation."
    else:
        duration, error = get_travel_duration(user_input[0], user_input[1], user_input[2])
        if duration:
            output = generate_output(user_input[0], user_input[1], user_input[2], duration)
        else:
            output = generate_output_error(error)

    return output


