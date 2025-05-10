import os
import csv
from .models import WEBSITES, Car

DATA_FIELDS = [key for key in Car.__annotations__.keys()]

for website_name, tbl in WEBSITES.items():
    output_path = f"./scraper/data/{website_name}.csv"
    if os.path.exists(output_path):
        os.remove(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames = DATA_FIELDS)
        writer.writeheader()

# You know it might be more organized to do car: Car
# But i don't wanna waste performance turning it to a car then back to a dict for writing
def WriteAuctionToSiteCSV(website_name, car: dict):
    output_path = f"./scraper/data/{website_name}.csv"
    
    with open(output_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames = DATA_FIELDS)
        writer.writerow(car)