import requests
import bs4

#request to get website code
res = requests.get('https://example.com/')
#makes the code readable
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup)

#equivalent to document.querySelector
title = soup.select('title')
#gets the content of the element without the tags
title_text = title[0].getText()
print(title_text)