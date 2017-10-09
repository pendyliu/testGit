# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 00:06:31 2017

@author: Administrator
"""


import urllib.request,re,os,demjson


#http://www.imooc.com/learn/177
ur = "http://m.imooc.com/learn/"+input("请输入课程的id号：")

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print (path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False
req = urllib.request.Request(url=ur)

res = urllib.request.urlopen(req)

data = res.read().decode('utf-8')  

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print ("%.2f%%"% percent)


for t in set(re.findall(r'(<title>课程-(.*?)</title>)', str(data))):
    print(t[1]+' 创建目录完成')
    #保存
    uiui=r'D:\python'+'\\'+t[1]
    mkdir(uiui)
    for t1 in set(re.findall(r'(<a data-id="(.*?)" href="/video/(.*?)">(.*?)</a>)', str(data))):
        ui='http://www.imooc.com/course/ajaxmediainfo/?mid='+ t1[1]+'&mode=flash'#解析的接口
        
        re8 = urllib.request.Request(url=ui)
        res = demjson.decode(urllib.request.urlopen(re8).read())
        qa=res['data']['result']['mpath']

        qw=qa[2].replace('http://v2','http://v1')#取下载链接
        aq=res['data']['result']['name']#取下载链接名字
        print(aq+qw)
        local = os.path.join(uiui,aq+".mp4") 
        urllib.request.urlretrieve(qw,local,callbackfunc) 

