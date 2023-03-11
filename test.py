import json

with open("config.json") as f:
    config = json.load(f)
url_com = config['comm']['url_com']

print(url_com)
