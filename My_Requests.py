import requests
import os
#通用代码框架 
def getHTMLText(url):
    try:
        hd={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        r=requests.get(url,timeout=30,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "连接错误！"

#提交Params数据 
def getHTMLText_Params(url):
    try:
        wd={'ip':'183.199.140.207'}
        hd={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        r=requests.get(url,timeout=30,headers=hd,params=wd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.request.url)
        return r.text
    except:
        return "连接错误！"

#下载二进制文件
def DownLoadPic(url):
    root='d://Pics//'
    path=root+url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                return print('创建成功')
        else:
            print('文件存在！')

    except:
        print('爬取异常')




if __name__ == "__main__":
    #https://www.baidu.com/s?wd=Python
    #http://200019.ip138.com/ 本机IP地址查询 取值区间 r.text[556:595]
    #http://www.ip138.com/ips138.asp?ip=183.199.140.207 查询指定IP地址 取值区间 r.text[-2387:-2150]
    url='https://python123.io/ws/demo.html'
    
    print(getHTMLText(url))
    