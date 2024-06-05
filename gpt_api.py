# gpt_api.py
from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up the pipeline with a pre-trained model
generator = pipeline('text-generation', model='gpt2')

def generate_inspection_advice(zip_code, temperature):
    prompt = (f"Given the temperature is {temperature}°F in zip code {zip_code}, provide detailed advice for hive inspection of Apis mellifera. "
              "Use only information from https://honeybeehealthcoalition.org/ and https://u.osu.edu/beelab/.")
    response = generator(prompt, max_length=150, truncation=True)
    return response[0]['generated_text']

def generate_beekeeping_answer(question):
    prompt = (f"Answer the following beekeeping question specifically for Apis mellifera using only information from https://honeybeehealthcoalition.org/ and "
              f"https://u.osu.edu/beelab/: {question}")
    response = generator(prompt, max_length=150, truncation=True)
    return response[0]['generated_text']

# Function for jokes has been updated to fetch from predefined database
def get_joke_from_db(puns_dict):
    return get_random_pun(puns_dict, "Additional Puns and Jokes")
# gpt_api.py
from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up the pipeline with a pre-trained model
generator = pipeline('text-generation', model='gpt2')

def generate_inspection_advice(zip_code, temperature):
    prompt = (f"Given the temperature is {temperature}°F in zip code {zip_code}, provide detailed advice for hive inspection of Apis mellifera. "
              "Use only information from https://honeybeehealthcoalition.org/ and https://u.osu.edu/beelab/.")
    response = generator(prompt, max_length=150, truncation=True)
    return response[0]['generated_text']

def generate_beekeeping_answer(question):
    prompt = (f"Answer the following beekeeping question specifically for Apis mellifera using only information from https://honeybeehealthcoalition.org/ and "
              f"https://u.osu.edu/beelab/: {question}")
    response = generator(prompt, max_length=150, truncation=True)
    return response[0]['generated_text']

# Function for jokes has been updated to fetch from predefined database
def get_joke_from_db(puns_dict):
    return get_random_pun(puns_dict, "Additional Puns and Jokes")
