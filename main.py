from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)
articles = soup.find_all(class_="titleline")
article_links = []
article_texts = []
for article in articles:
    link = article.a.get("href")
    text = article.get_text()
    article_links.append(link)
    article_texts.append(text)

up_votes = [int(upvote.get_text().split()[0]) for upvote in soup.find_all(class_="score")]

print(article_texts[up_votes.index(max(up_votes))])
print(article_links[up_votes.index(max(up_votes))])
print(max(up_votes))












# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# all_anchor = soup.findAll('a')
#
# # for tag in all_anchor:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="heading")
# company_url = soup.select_one(selector="p a")
#
# # print(company_url)

