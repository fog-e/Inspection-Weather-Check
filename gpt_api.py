# gpt_api.py
from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up the pipeline with a pre-trained model
generator = pipeline('text-generation', model='gpt2')

def generate_inspection_advice(zip_code, temperature):
    prompt = (f"Given the temperature is {temperature}°F in zip code {zip_code}, provide detailed advice for hive inspection. "
              "Use information from https://honeybeehealthcoalition.org/ and https://u.osu.edu/beelab/.")
    response = generator(prompt, max_length=150, truncation=True)
    return response[0]['generated_text']

def generate_beekeeping_answer(question):
    prompt = (f"Answer the following beekeeping question using information from https://honeybeehealthcoalition.org/ and "
              f"https://u.osu.edu/beelab/: {question}")
    response = generator(prompt, max_length=150, truncation=True)
    return response[0]['generated_text']

def generate_joke():
    prompt = "Tell me a bee-themed joke that is culturally sensitive and inclusive."
    response = generator(prompt, max_length=50, truncation=True)
    return response[0]['generated_text']
