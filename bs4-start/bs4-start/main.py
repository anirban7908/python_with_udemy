from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

articles = soup.find_all(name='a', class_="storylink")
article_text = []
article_link = []

for article_tag in articles:
    article_text.append(article_tag.getText())
    article_link.append(article_tag.get('href'))

upvote_text = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# pprint(article_text)
# pprint(article_link)
max_number = max(upvote_text)
max_index = upvote_text.index(max_number)
pprint(article_text[max_index])
pprint(article_link[max_index])
pprint(max_number)



# with open("website.html") as htmlfile:
#     content = htmlfile.read()

# soup = BeautifulSoup(content, 'html.parser')

# # print(soup.title)

# anchor_tags = soup.find_all_all(name='a')


# for a in anchor_tags:
#     # print(a)
#     # get inner text of element
#     # print(a.getText())

#     # get attributre value of an element
#     # print(a.get("href"))
#     pass

# # get a single element from many same elements
# # ele = soup.find_all(name="h1", id="name")
# # print(ele)


# # Get element by classname

# # ele_class = soup.find_all(name='h3', class_="heading")
# # print(ele_class.getText())

# # Get items via selectors
# # css selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)

# # id selectors
# company_url2 = soup.select_one(selector="#name")
# print(company_url2)

# # class selectors
# company_url3 = soup.select(selector=".heading")
# print(company_url3)