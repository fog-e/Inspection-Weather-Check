# test_openai.py
from gpt_api import generate_text

def test_gpt():
    try:
        result = generate_text("Tell me a joke")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    test_gpt()
