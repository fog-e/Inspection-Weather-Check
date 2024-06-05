# repl.py
from gpt_api import generate_beekeeping_answer, get_joke_from_db
from file_io import load_puns, get_random_pun, log_inspection_to_csv

# Load the puns from the CSV file
puns_dict = load_puns('bee_puns.csv')

def get_weather_info():
    temperature = float(input("Enter the current temperature (in °F): "))
    return temperature

def check_temperature(temperature):
    if temperature < 60 or temperature > 90:
        return False
    return True

def get_hive_condition():
    queen_sighted = input("Did you see the queen? (yes/no): ")
    brood_pattern = input("How is the brood pattern? (good/poor): ")
    honey_stores = input("Are there sufficient honey stores? (yes/no): ")
    pests_or_diseases = input("Did you notice any pests or diseases? (yes/no): ")
    eggs_and_larvae = input("Were eggs and larvae present? (yes/no): ")
    capped_brood = input("Was there capped brood? (yes/no): ")
    other_observations = input("Any other observations? (text): ")

    condition = {
        "queen_sighted": queen_sighted,
        "brood_pattern": brood_pattern,
        "honey_stores": honey_stores,
        "pests_or_diseases": pests_or_diseases,
        "eggs_and_larvae": eggs_and_larvae,
        "capped_brood": capped_brood,
        "other_observations": other_observations
    }
    return condition

def repl():
    print("Hello there, bee-autiful beekeeper! 🐝")
    while True:
        print("Please choose an option:")
        print("1. Get inspection advice")
        print("2. Log inspection details")
        print("3. Ask a beekeeping question")
        print("4. Tell me a joke")
        print("5. Exit")
        choice = input("> ").strip().lower()

        if choice == '1':
            temperature = get_weather_info()
            if not check_temperature(temperature):
                print("Oh honey, it's not the best day for an inspection. The temperature is outside the optimal range for hive inspections.")
                if input("Would you like to hear a joke? (yes/no): ").strip().lower() == 'yes':
                    joke = get_joke_from_db(puns_dict)
                    print(joke)
            else:
                print("It's a go for suiting up and inspecting! Remember to look for queenright status, eggs and larvae, capped brood, food stores, and any signs of varroa or disease.")
        elif choice == '2':
            zip_code = input("Please enter your 5-digit zip code: ")
            hive_condition = get_hive_condition()
            log_inspection_to_csv('inspection_log.csv', zip_code, hive_condition)
            print("Inspection details have been logged.")
        elif choice == '3':
            question = input("What is your beekeeping question? ")
            answer = generate_beekeeping_answer(question)
            print(answer)
        elif choice == '4':
            joke = get_joke_from_db(puns_dict)
            print(joke)
        elif choice == '5':
            print("Bee seeing you! Don't bee a stranger!")
            break
        else:
            print("Unrecognized action detected. For a list of all available hive commands, type 'help'.")

if __name__ == '__main__':
    repl()
