from utils import *
from pprint import pprint

DATA_PATH = "data/claims.json"

def load_claims():
    return read_from_json(DATA_PATH)

def save_claims(records):
    write_to_json(records, DATA_PATH)

def view_all_claims():
    results =  load_claims()
    pprint(results)