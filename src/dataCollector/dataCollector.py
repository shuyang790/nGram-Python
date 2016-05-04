#!/usr/bin/python
import os, time
import re
import urlparse
import requests
from bs4 import BeautifulSoup

agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"

class Spider():
    def __init__(self, year, month, day):
        self.host = "http://news.sina.com.cn/"
        self.url = "http://news.sina.com.cn/old1000/news1000_" + str(year) + str(month).zfill(2) + str(day).zfill(2) + ".shtml"
        self.year = year
        self.month = month
        self.day = day
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': agent})
        self.s.headers.update({'Referer': self.host })

    def parse_list(self):
        r = self.s.get(self.url)
#        print r.content
        soup = BeautifulSoup(r.content.decode('gbk','ignore'), 'lxml' )
        tags = soup.select("ul li a")
        for _tag in tags:
            tag = str(_tag)
            start = len("<a href=\"")
            end = start + 1
            while tag[end] != '"':
                end += 1
            url = tag[start:end]
            if not url.startswith("http"):
                url = "http://news.sina.com.cn" + url
            if url.find("cgi-bin") != -1:
                continue
            print "Crawl:",  url
            num_try = 0
            get_content = 0
            while get_content == 0:
                try:
                    page_r = self.s.get(url)
                    get_content = 1
                except:
                    time.sleep(2)
                    num_try += 1
                    if num_try > 10:
                        break
            if num_try > 10:
                continue
            page_soup = BeautifulSoup(page_r.content.decode('gbk', 'ignore'), 'lxml')
            find_res = page_soup.find_all("font", id="zoom")
            if len(find_res) == 0:
                print "No Content"
                continue
#            print page_r.content
            content = ""
            for tag in page_soup.select("#zoom > p"):
                print tag
                content += str(tag)
            f = open("results/" + str(self.year) + str(self.month).zfill(2) + str(self.day).zfill(2) + ".txt", "a")
            f.write(content)
            f.close()
            print r.content[:20]

def main():
    print "Welcome!"
    year = 2006
    month = 4
    os.system("mkdir results")
    for day in range(1, 31):
        if month == 2 and day > 28:
            break
        spider = Spider(year, month, day)
        spider.parse_list()
    pass

if __name__ == "__main__":
    main()
