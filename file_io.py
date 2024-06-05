# file_io.py
import csv
import random

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def load_puns(file_path):
    puns_dict = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            point = row["Interaction Point"]
            pun = row["Pun or Joke"]
            if point not in puns_dict:
                puns_dict[point] = []
            puns_dict[point].append(pun)
    return puns_dict

def get_random_pun(puns_dict, point):
    return random.choice(puns_dict.get(point, ["No puns available."]))
