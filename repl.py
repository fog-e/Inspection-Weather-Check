# repl.py
from gpt_api import generate_inspection_advice, generate_beekeeping_answer, generate_joke
from file_io import load_puns, get_random_pun

# Load the puns from the CSV file
puns_dict = load_puns('bee_puns.csv')

def get_weather_info():
    temperature = float(input("Enter the current temperature (in °F): "))
    return temperature

def get_hive_condition():
    condition = input("Describe the hive condition (e.g., 'good brood pattern, sufficient honey stores'): ")
    return condition

def repl():
    print(get_random_pun(puns_dict, "Friendly Greeting"))
    zip_code = input("Please enter your 5-digit zip code to check the weather: ")
    temperature = get_weather_info()
    advice = generate_inspection_advice(zip_code, temperature)
    print(advice)

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
                  "ask a beekeeping question - Get an answer to a beekeeping question\n"
                  "tell me a joke - Hear a bee-themed joke")
        elif command == 'weather check':
            temperature = get_weather_info()
            advice = generate_inspection_advice(zip_code, temperature)
            print(advice)
        elif command == 'inspection log':
            hive_condition = get_hive_condition()
            log_entry = f"Inspection Log: {hive_condition}"
            print(log_entry)
        elif command == 'ask a beekeeping question':
            question = input("What is your beekeeping question? ")
            answer = generate_beekeeping_answer(question)
            print(answer)
        elif command == 'tell me a joke':
            joke = generate_joke()
            print(joke)
        else:
            print("Unknown command. Type 'help' for a list of available commands.")

if __name__ == '__main__':
    repl()
