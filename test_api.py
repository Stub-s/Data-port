import requests
response = requests.get('https://graphql.anilist.co')
print(response.status_code)