# -*- coding:utf-8 -*-
import re
import requests
import sys
import os

#超详细的注释，用于最基本爬虫的学习

#请求头
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

#帖子地址
#aUrl="https://tieba.baidu.com/p/3218895950"  

#使用提示
print('----------百度贴吧图片下载器，Made by MINU----------')
print('')
print('输入帖子地址，按下回车开始')
aUrl=input()

#计算变量
i=1   #图片总数，用于计算和命名
k=1   #当前页数
c=1   #总页数




#实现每页查找的总循环
while k==1 or k<=c:         #从第一页开始找，直到最后一页
    x=0             #引用list d 的元素，每页开始重置

    f=1   #当前下载页的进度

    k=str(k)             #转换k的类型
    url=aUrl+"?pn="+k   #帖子的第几页
    k=int(k)    

    html=requests.get(url,headers)     #通过请求得到网页
    
    
    
    b=re.findall('<span class="red">(.*?)</span>',html.text,re.S)   #获取页数,b为一个列表list
    c=int(b[0])        #帖子总页数为c，转换列表元素为整数

    if k==1:      #只在查找的第一页的时候，提示帖子页数
        print(u"该贴共",c,u"页")
        wenjianjia = re.findall(r"\d{10}",html.text)
        path = "C:\\Users\\minu\\Desktop\\"+wenjianjia[0]
        #判断目录是否存在
        exist=os.path.exists(path)
        if exist==False:
        	os.makedirs(path)
        
        
    a=re.findall('http.*?://img.*?.baidu.com/forum/w%3D580/sign=.*?([a-zA-Z0-9]{40}).jpg',html.text,re.S)     #查找图片地址，保存为list a
    d=list(set(a))   #list转换成set，去除重复；set再转换成有序的list，便于引用
    e=len(d)  #取list d 的长度，为每页的图片数
    #提示
    print("")
    print(u"第",k,u"页，共",len(d),u"张图片")

    #保存图片的循环
    while e>0 and x<e:
        url="http://imgsrc.baidu.com/forum/pic/item/"+d[x]+".jpg"  #通过小图地址，加上规则，得到大图地址

        #一个原行刷新的提示
        sys.stdout.write( "当前页下载进度[%3d],"%f)
        sys.stdout.flush()
        sys.stdout.write("总进度[%3d]\r"%i)
        sys.stdout.flush()
        
        #print (u"图片",i,)   #下载进度
        r = requests.get(url,stream=True)   # 获取图片，stream参数不理解
        i=str(i)  #转字符，用于命名

        
    	#保存图片
        filename = path +"\\"+ i + ".jpg"  #文件名使用绝对路径 
        with open(filename,'wb') as fd:    #wd 以二进制模式打开
            for chunk in r.iter_content():
                fd.write(chunk)   
        i=int(i)
        i=i+1
        x=x+1
        f=f+1
    k=k+1
print("")
print(u"下载完成")
input()

        

    





 
    















