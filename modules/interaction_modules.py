import json

with open("questions/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def fetch_data(index):
    return data[index]["item"], data[index]["options"]


def verify_response(index, user_response):
    return user_response == data[index]["correct_option_index"]


def get_data_count():
    return len(data)
