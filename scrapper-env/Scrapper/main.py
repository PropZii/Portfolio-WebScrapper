import requests
from bs4 import BeautifulSoup


url = "https://www.atlas-monde.net/tous-les-pays/"

response = requests.get(url)

print(response)
# if response.ok:
#     print(response.text)
