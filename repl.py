# repl.py
import sys
from gpt_api import generate_text
from file_io import load_puns, get_random_pun

# Load the puns from the CSV file
puns_dict = load_puns('bee_puns.csv')

def repl():
    print(get_random_pun(puns_dict, "Friendly Greeting"))
    zip_code = input("Please enter your 5-digit zip code to check the weather: ")
    prompt = f"Provide weather advice for beekeeping in zip code {zip_code}"
    try:
        result = generate_text(prompt)
        print(get_random_pun(puns_dict, "Optimal Conditions Feedback") if "sunny" in result else get_random_pun(puns_dict, "Non-Optimal Conditions Feedback"))
    except Exception as e:
        print(f"An error occurred: {e}")

    while True:
        command = input("> ").strip().lower()

        if command == 'exit':
            print(get_random_pun(puns_dict, "Sign Off"))
            break
        elif command == 'help':
            print("Available commands:\n"
                  "help - Show this help message\n"
                  "exit - Exit the application\n"
                  "weather check - Check the weather for inspection\n"
                  "inspection log - Log inspection details\n"
                  "tell me a joke - Hear a bee-themed joke")
        elif command == 'weather check':
            zip_code = input(get_random_pun(puns_dict, "Request Zip Code"))
            prompt = f"Provide weather advice for beekeeping in zip code {zip_code}"
            try:
                result = generate_text(prompt)
                print(get_random_pun(puns_dict, "Optimal Conditions Feedback") if "sunny" in result else get_random_pun(puns_dict, "Non-Optimal Conditions Feedback"))
            except Exception as e:
                print(f"An error occurred: {e}")
        elif command == 'tell me a joke':
            print(get_random_pun(puns_dict, "Additional Puns and Jokes"))
        else:
            print("Unknown command. Type 'help' for a list of available commands.")

if __name__ == '__main__':
    repl()
