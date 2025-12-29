import json
import csv

def load_testdata(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def load_csvtestdata(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data