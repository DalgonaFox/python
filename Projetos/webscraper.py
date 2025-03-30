from bs4 import BeautifulSoup
import requests
import csv # Para transformar os dados em uma tabela do Excel.
import re

quotespage = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(quotespage.text, "html.parser")
quotes = soup.find_all("span", attrs={"class":"text"}) # Procura todos que tem a tag "span" e o atributo classe='text'.
authors = soup.find_all("small", attrs={"class":"author"})

with open("scraped_quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + " . " + author.text)
    writer.writerow([quote.text, author.text])
file.close()

palavras = soup.find_all(string=re.compile("woman")) # Procura palavras no site inteiro.

for palavra in palavras:
    print(palavra.text)