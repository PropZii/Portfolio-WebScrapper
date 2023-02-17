import requests
from bs4 import BeautifulSoup


url = input("Entrer un url: ")

response = requests.get(url)


if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
