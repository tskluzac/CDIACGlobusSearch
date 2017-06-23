import json

with open('cdiac_gmeta_index2.json', 'r') as json_data:
    gmeta = json.load(json_data)
    json_data.close()

