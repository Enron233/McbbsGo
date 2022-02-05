import requests
from bs4 import BeautifulSoup

myHeader = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}


def getServerUrl(pageNum):
    url = "http://www.mcbbs.net/forum-server-" + str(pageNum) + ".html"
    resp = requests.get(url, headers=myHeader)
    contain = BeautifulSoup(resp.text, "html.parser")
    firstFind = contain.find("table", attrs={"summary": "forum_179"})
    secondFind = firstFind.find_all("tbody")
    resp.close()
    return secondFind
