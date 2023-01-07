import requests
import json
import os
import pandas as pd

FILE_NAME = "sample.json"
API_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetAllManufacturers?format=json&page=2"

def read_data():
    with open(FILE_NAME, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object

def check_if_data_is_downloaded():
    if os.path.exists(FILE_NAME):
        return read_data()
    else:
        return False

def store_data(result_json):
    
    with open(FILE_NAME, "w") as outfile:
        json.dump(result_json, outfile)
    
def process_data():

    data = read_data()

    country_list = []
    mfr_name = []

    for maker in data:
        if maker["Country"]:
            country_list.append(maker["Country"])
            mfr_name.append(maker["Mfr_Name"])

    df = pd.DataFrame({
        "Country": country_list,
        "Manufacturer Name": mfr_name
    })

    df = df["Country"].value_counts().reset_index()

    df.columns =['Country', 'Number of Manufacturers']

    return df


def fetch_data():

    data = check_if_data_is_downloaded()

    if not data:
        data = requests.get(API_URL).json()
        store_data(data["Results"])
    
    df = process_data()

    return df