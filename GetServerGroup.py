import requests
from bs4 import BeautifulSoup

import GetServerList


def GetServerGroup(url):
    resp = requests.get(url, headers=GetServerList.myHeader)
    contain = BeautifulSoup(resp.text, "html.parser")
    firstFind = contain.find("table", attrs={"summary": "分类信息"})
    secondFind = firstFind.find_all("td")
    return secondFind[13].text
