import requests
from bs4 import BeautifulSoup

import GetServerList


def GetServerGroup(uid):
    url = f"https://www.mcbbs.net/forum.php?mod=viewthread&tid={uid}"
    resp = requests.get(url, headers=GetServerList.myHeader)
    contain = BeautifulSoup(resp.text, "html.parser")
    firstFind = contain.find("table", attrs={"summary": "分类信息"})
    secondFind = firstFind.find_all("td")
    return secondFind[13].text


def GetServerTitle(uid):
    url = f"https://www.mcbbs.net/forum.php?mod=viewthread&tid={uid}"
    resp = requests.get(url, headers=GetServerList.myHeader)
    contain = BeautifulSoup(resp.text, "html.parser")
    firstFind = contain.find("span", attrs={"id": "thread_subject"})
    return firstFind.text
