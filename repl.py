# repl.py
import sys
from gpt_api import generate_text
from file_io import read_file, write_file, load_puns, get_random_pun
import csv

# Load the puns from the CSV file
puns_dict = load_puns('bee_puns.csv')

def log_inspection_details():
    details = {}
    details["Date"] = input("Enter the date of inspection (YYYY-MM-DD): ")
    details["Time"] = input("Enter the time of inspection (HH:MM): ")
    details["Temperature"] = input("Enter the temperature during inspection: ")
    details["Wind Speed"] = input("Enter the wind speed during inspection: ")
    details["Precipitation"] = input("Enter the precipitation during inspection: ")
    details["Queen Sighted"] = input("Did you spot the queen? (Yes/No): ")
    details["Brood Pattern"] = input("How's the brood pattern? (Good/Poor): ")
    details["Honey Stores"] = input("Are there enough honey stores? (Yes/No): ")
    details["Pests or Diseases"] = input("Any pests or diseases spotted? (Yes/No): ")
    details["Eggs and Larvae"] = input("Did you see eggs and larvae? (Yes/No): ")
    details["Capped Brood"] = input("Is there capped brood in the hive? (Yes/No): ")
    details["Other Observations"] = input("Any other observations? (Text input): ")

    with open('inspection_log.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=details.keys())
        if csvfile.tell() == 0:
            writer.writeheader()  # Write header only if file is empty
        writer.writerow(details)

    print("Inspection details logged.")

def tell_joke():
    joke = get_random_pun(puns_dict, "Additional Puns and Jokes")
    print(joke)

def repl():
    print(get_random_pun(puns_dict, "Friendly Greeting"))
    print("Please enter your 5-digit zip code to check the weather.")

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
            result = generate_text(prompt)
            print(get_random_pun(puns_dict, "Optimal Conditions Feedback") if "sunny" in result else get_random_pun(puns_dict, "Non-Optimal Conditions Feedback"))
        elif command == 'inspection log':
            log_inspection_details()
        elif command == 'tell me a joke':
            tell_joke()
        else:
            print("Unknown command. Type 'help' for a list of available commands.")

if __name__ == '__main__':
    repl()
