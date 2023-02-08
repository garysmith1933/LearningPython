import requests
import bs4

res = requests.get('http://quotes.toscrape.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')

authors = set()

for author in soup.select('.author'):
  authors.add(author.text)

print(authors)


quotes_list = []
quotes = soup.select('.text')

for quote in soup.select('.text'):
  quotes_list.append(quote.text)

print(quotes_list)

for tag in soup.select('.tags-box .tag'):
  print(tag.text)

url = 'http://quotes.toscrape.com/page/'

authors = set()


for page in range(1,10):
  page_url = url+str(page)
  res = requests.get(page_url)
  soup = bs4.BeautifulSoup(res.text,'lxml')

  for name in soup.select(".author"):
    authors.add(name.text)
    
print(authors)