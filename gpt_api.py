# gpt_api.py
from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the Hugging Face API token from the environment variables
api_token = os.getenv('HUGGINGFACE_API_TOKEN')
if not api_token:
    raise ValueError("Hugging Face API token not found. Make sure it is set in the .env file.")

# Set up the pipeline with a pre-trained model
generator = pipeline('text-generation', model='gpt-3.5-turbo', api_key=api_token)

def generate_text(prompt):
    response = generator(prompt, max_length=50)
    return response[0]['generated_text']
git 