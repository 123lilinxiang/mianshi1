#这个问题不太会做
#还没有接触过调用网页进行数据分析
#不好意思~~

import urllib.request

def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def saveHtml(file_name,file_content):

    with open(file_name.replace('/','_')+'.html','wb') as f:
        f.write(file_content)
        html = getHtml("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#t")
        saveHtml("test",html)