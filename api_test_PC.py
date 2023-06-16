import requests
import json
import pandas as pd
import numpy as np

query = '''
    query ($id: Int) {
        Media (id: $id, type: ANIME) {
            id
            title {
                romaji
                english
                native
            }
        }
    }
'''

variables = {
    'id': 15125
}

url = 'https://graphql.anilist.co'
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.json())