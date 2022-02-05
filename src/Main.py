import time

import GetServerGroup
import GetServerList


f = open("ServerList.txt", mode="a", encoding="UTF-8")


def getServerInfo(pageNum):
    result = GetServerList.getServerUrl(pageNum)
    if pageNum == 1:
        for deal in result[3:]:
            firstDeal = deal['id']
            postUid = firstDeal[13:]
            postUrl = f"https://www.mcbbs.net/thread-{postUid}-1-1.html"
            f.write("\n" + GetServerGroup.GetServerTitle(postUid) + "\n帖子地址: " + str(postUrl) + "\n联系方式: " + GetServerGroup.GetServerGroup(postUid))
            print("\n" + GetServerGroup.GetServerTitle(postUid) + "\n帖子地址: " + str(postUrl) + "\n联系方式: " + GetServerGroup.GetServerGroup(postUid))
        pass
    else:
        for deal in result[1:]:
            firstDeal = deal['id']
            postUid = firstDeal[13:]
            postUrl = f"https://www.mcbbs.net/thread-{postUid}-1-1.html"
            f.write("\n" + GetServerGroup.GetServerTitle(postUid) + "\n帖子地址: " + str(postUrl) + "\n联系方式: " + GetServerGroup.GetServerGroup(postUid))
            print("\n" + GetServerGroup.GetServerTitle(postUid) + "\n帖子地址: " + str(postUrl) + "\n联系方式: " + GetServerGroup.GetServerGroup(postUid))
        pass


print("欢迎使用MCBBS服务器提取器，提取原理为Python爬虫，仅供学习交流使用~")
time.sleep(1)
print("如果你在使用过程中遇到bug、问题，或者想与作者一起交流探讨，欢迎添加QQ: 286526681 or 进入Github and star me！OVO！")
time.sleep(2)
print('''
==================================
    当前目标：MCBBS我的世界中文论坛
    目标板块：服务器板块
==================================
''')
start = int(input("请输入起始页："))
end = int(input("请输入终止页："))
print(f"开始爬取服务器板块第{start}页到{end}页的服务器帖")
while start <= end:
    getServerInfo(start)
    print("===============================")
    print(f"第{start}页服务器信息爬取成功")
    print("===============================")
    start = start + 1
    continue
f.close()
input("爬取成功，已经保存到本程序同目录ServerList.txt中，如需再次使用请删除目录中ServerList.txt")