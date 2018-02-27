import requests
from bs4 import BeautifulSoup
from copy import deepcopy
#
url = "https://google.com"
response = requests.get(url)

# print(response.headers)
content = response.content

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

# print(soup.title.string)

# all_a = soup.find_all("a")
# for x in all_a:
#    print(x)


all_a_https = soup.find_all("a")
# print(all_a_https)
for x in all_a_https:
    print(x)

# print(all_a_https[0])

# my_string = deepcopy(all_a_https[0])
# print(my_string)

# data = {}
# for a in all_a_https:
#     title = a.string.strip()
#     data[title] = a.attrs['href']
#
# print(data)
