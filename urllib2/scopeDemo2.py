# -*- coding:utf-8 -*-
#import urllib
import urllib.request
import re


# page = 2
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
url='https://www.qiushibaike.com/article/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'
accept='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
referer='https://www.qiushibaike.com/'
headers = {'User-Agent': user_agent,'Accept':accept,'Referer':referer}
try:
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    pattern = re.compile('<div .*?author clearfix">.*?<a .*?<img .*?</a>.*?<a .*?><h2>(.*?)</h2>.*?</a>',re.S)
    # pattern=re.compile('author clearfix')
    items=re.findall(pattern=pattern,string=content)
    for item in items:
        print(item[0])
except urllib.request.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)