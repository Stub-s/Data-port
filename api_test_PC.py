import requests
import json
import pandas as pd
import numpy as np

query = '''
    query ($id: Int, $page: Int, $perPage: Int, $search: String) {
        Page (page: $page, perPage: $perPage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media (id: $id, search: $search) {
                id
                title {
                    romaji
                }
            }
        }
    }
}
'''

variables = {
    'search': 'Boku no Hero Academia',
    'page': 1,
    'perPage': 10
}

url = 'https://graphql.anilist.co'
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.json())
