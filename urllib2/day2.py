import urllib2
import urllib.parse
import urllib.request
#  python 2.7里面的写法
# def download(url,user_agent='wswp',num_retries=2):
#     print('Downloading:',url)
#     headers={'User-agent':user_agent}
#     request=urllib2.request(url,headers)
#     try:
#         html=urllib2.urlopen(request).read()
#     except urllib2.URLError as e:
#         print('Download Error:',e.reason)
#         html=None
#     if num_retries>0:
#         if hasattr(e,'code') and 500<=e.code<600:
#             return download(url,user_agent,num_retries)
#     return html

# python3.6里面的写法

url = 'http://www.baidu.com/s'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'WHY',
         'location' : 'SDU',
         'language' : 'Python',
         'ie' : 'utf-8',
         'wd' : 'python' }
headers = { 'User-Agent' : user_agent }
data = urllib.parse.urlencode(values)
#data=data.encode(encoding='UTF8')
req = urllib.request.Request(url+'?'+data)
#, data, headers)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode('UTF8'))

# res=download('http://www.shinnet.cn')
# print(res)