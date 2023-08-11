from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)
first_title = soup.find(class_="titleline")
first_link = first_title.a.get("href")
first_upvote = soup.find(class_="score")

print(first_title.get_text(), first_link, first_upvote.get_text())






















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

