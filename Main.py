import datetime
import time

import GetServerGroup
import GetServerList

r = open("ServerList.txt", mode="w", encoding="UTF-8")
f = open("ServerList.txt", mode="a", encoding="UTF-8")


def getServerInfo(pageNum):
    result = GetServerList.GetServerUrl(pageNum)
    for deal in result:
        firstDeal = deal['href']
        secondDeal = firstDeal.split("&")
        gPostUrl = "http://www.mcbbs.net/" + firstDeal
        postUrl = "http://www.mcbbs.net/&" + secondDeal[1]
        serverName = deal.text
        f.write("\n" + serverName + "\n帖子地址: " + str(postUrl) + "\n联系方式: " + GetServerGroup.GetServerGroup(gPostUrl))
    pass


print("欢迎使用MCBBS服务器提取器，提取原理为Python爬虫，仅供学习交流使用~")
time.sleep(2)
print("如果你在使用过程中遇到bug、问题，或者想与作者一起交流探讨，欢迎添加QQ: 286526681 or 进入Github and star me！OVO！")
time.sleep(3)
print('''
==================================
    当前目标：MCBBS我的世界中文论坛
    目标板块：服务器板块
==================================
''')
time.sleep(1)
start = int(input("请输入起始页："))
time.sleep(1)
end = int(input("请输入终止页："))
print(f"开始爬取服务器板块第{start}页到{end}页的服务器帖")
r.write("此次数据爬取时间：" + datetime.datetime.now().strftime('%Y-%m-%d %M:%S'))
r.close()
while start <= end:
    getServerInfo(start)
    print(f"第{start}页服务器信息爬取成功")
    start = start + 1
    continue
input("爬取成功，已经保存到本程序同目录ServerList.txt中")

