import csv

def load_puns(filename):
    puns_dict = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print(f"Headers: {reader.fieldnames}")  # Debugging step
        if 'Category' not in reader.fieldnames or 'Pun' not in reader.fieldnames:
            raise ValueError("CSV file does not have the required 'Category' and 'Pun' columns.")
        
        for row in reader:
            print(row)  # Debugging step
            category = row['Category']
            if category not in puns_dict:
                puns_dict[category] = []
            puns_dict[category].append(row['Pun'])
    return puns_dict

def get_random_pun(puns_dict, category):
    import random
    if category in puns_dict:
        return random.choice(puns_dict[category])
    else:
        return "No pun available for this category."

def log_inspection_to_csv(filename, zip_code, hive_condition):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([zip_code, hive_condition["queen_sighted"], hive_condition["brood_pattern"], 
                         hive_condition["honey_stores"], hive_condition["pests_or_diseases"], 
                         hive_condition["eggs_and_larvae"], hive_condition["capped_brood"], 
                         hive_condition["other_observations"]])
