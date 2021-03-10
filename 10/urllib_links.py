import re
from urllib import request


def searchLinks(link):
    LinksList = []
    reg = request.Request(link)
    response = request.urlopen(reg)
    wep_page = response.read()
    res = re.findall(r'href="(http(s?)://.*?)"', str(wep_page))
    for i in res:
        LinksList.append(i)
    return LinksList


print(searchLinks("https://yandex.ru/"))
