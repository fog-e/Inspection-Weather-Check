# test_openai.py
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def test_openai():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me a joke"}
            ]
        )
        print(response.choices[0].message['content'])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    test_openai()
