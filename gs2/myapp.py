import requests
import json

URL ="http://127.0.0.1:8000/create/"

data = {
    'name':'brij',
    'roll':'21',
    'city':'bokaro',
}

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)