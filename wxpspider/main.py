# coding:utf-8
'''
搜索微信公众号：http://weixin.sogou.com/weixin?type=1 &    query=keyword  &  page = %d
搜索微信文章:  http://weixin.sogou.com/weixin?type=2  & query=keyword & page = %d

# '''
import json
import sys

from bs4 import BeautifulSoup
from PyQt4.QtCore import QByteArray, QString, QUrl
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView
from PyQt4.QtNetwork import QNetworkRequest


class Browser(QWebView):
    def __init__(self):
        self.currenttype = 1  # 1 = 搜索公众号 2 = 文章搜索 3 公众号主页 4 文章详情页
        QWebView.__init__(self)
        self.page().userAgentForUrl = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
        self.loadFinished.connect(self._loadFinish)

    def searchWxArticle(self, url):
        self.currenttype = 2
        self.page().mainFrame().load(url)

    def searchWxService(self, url):
        self.currenttype = 1
        self.page().mainFrame().load(url)
    def parseWxNumberHome(self,url):
        self.currenttype = 3
        self.page().mainFrame().load(url)

    def parseWxArticle(self,url):
        self.currenttype = 4
        self.page().mainFrame().load(url)

    def _loadFinish(self, ok):
        frame = self.page().mainFrame()
        # parse(frame.toPlainText())
        # print unicode(frame.toHtml()).encode('utf-8')
        # 1 = 搜索公众号 2 = 文章搜索
        if self.currenttype == 1:
            parseSearchWxService(frame.toHtml())
        elif self.currenttype == 2:
            parseSearchWxArtcle(frame.toHtml())
        elif self.currenttype == 3:
            parseWxServiceHome(frame.toHtml())
        elif self.currenttype == 4:
            parseWxArticleHome(frame.toHtml())

def parseWxArticleHome(content):
    content = unicode(content)
    soup = BeautifulSoup(content,"html5lib")
    wxArticleInfo = {}
    wxArticleInfo['title'] = soup.find("h2",{"class":"rich_media_title"}).text
    wxArticleInfo['content'] = repr(soup.find("div",{"class":"rich_media_content"}))

    print wxArticleInfo['content']
    # print json.dumps(wxArticleInfo)
def parseWxServiceHome(content):
    content = unicode(content)
    soup = BeautifulSoup(content,"html5lib")
    wxServiceInfo = {}
    wxServiceInfo['name'] = soup.find("strong",{"class":"profile_nickname"}).text
    wxServiceInfo['number'] = soup.find("p",{"class":"profile_account"}).text
    # 找到公众号的简介
    wxServiceIntro = []
    wxServiceIntroDiv = soup.find("ul",{"class":"profile_desc"}).find_all("li")
    for x in wxServiceIntroDiv:
        introInner = {x.find("label",{"class":"profile_desc_label"}).text:x.find("div",{"class":"profile_desc_value"}).text}
        wxServiceIntro.append(introInner)
    #找到所有公众号文章

    wxArticles = []
    for x in soup.find_all("div",{"class":"appmsg"}):
        wxArticle = {}
        wxArticle['title'] = x.find("h4",{"class":"weui_media_title"}).text
        wxArticle['image'] = x.find('span',{"class","weui_media_hd"}).attrs['style']
        wxArticle['url'] = 'http://mp.weixin.qq.com' + x.find("h4",{"class":"weui_media_title"}).attrs['hrefs']
        wxArticles.append(wxArticle)
    print json.dumps(wxArticles)
    # print json.dumps(wxServiceIntro)
    # wxServiceInfo['intro'] = soup.find("div",{"class","profile_desc_value"}).attrs['title']
    # wxServiceInfo['verfy_info'] = soup.find("div",{"class":"profile_desc_value"})


def parseSearchWxService(content):
    content = unicode(content)
    soup = BeautifulSoup(content, "html5lib")
    wxServiceS = soup.find_all('div', {'class': 'wx-rb'})
    # print soup.body
    # print wxServiceS
    data = []
    for wxServiceEnty in wxServiceS:
        wxResult = {}
        wxResult['url'] = wxServiceEnty.attrs['href']
        wxResult['head_image'] = wxServiceEnty.find('img').attrs['src']
        wxResult['name'] = wxServiceEnty.find('h3').text
        wxResult['number'] = wxServiceEnty.find('label', {'name': 'em_weixinhao'}).text
        wxResult['qrcode'] = wxServiceEnty.find('img', {'data-type': 'qr'}).attrs['src'];
        wxExtra = {}
        extra_datas = wxServiceEnty.find('div', {'class', 'txt-box'}).find_all('p', {'class': 's-p3'})
        # print extra_datas
        for extra_data in extra_datas:
            # print extra_data
            wxExtra[extra_data.find('span', {'class': 'sp-tit'}).text] = extra_data.find('span',
                                                                                         {'class': 'sp-txt'}).text
        wxResult['extra'] = wxExtra
        # print json.dumps(wxResult)
        data.append(wxResult)
    print json.dumps(data)


def parseSearchWxArtcle(content):
    content = unicode(content)
    f = open("./test.html", "w")
    # f.write(content.toUtf8())
    # f.close()
    # print content
    soup = BeautifulSoup(content, "html5lib")
    # print soup.title
    # print soup.body
    content = soup.find('div', {'class': 'results'})
    # if (content != None):
    # f.write(str(content))
    # f.close()
    wxArticle = content.find_all('div', {'class': 'wx-rb'})
    # x = 0;
    data = []
    for entry in wxArticle:
        wxResult = {}
        image_div = entry.find('div', {'class': 'img_box2'})
        # print image_div.find('img').attrs['src']
        wxResult['image'] = image_div.find('img').attrs['src']
        link_div = entry.find('div', {'class': 'txt-box'}).find('h4').find('a')
        # print link_div
        wxResult['title'] = link_div.text
        wxResult['url'] = link_div.attrs['href']
        data.append(wxResult)
        # data[x] = wxResult
        # x += 1
    print json.dumps(data)
    return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    type = 1
    keyword = u"搞笑"
    page = 1
    view = Browser()
    url = QUrl('http://weixin.sogou.com/weixin')
    # 搜索微信文章 test
    if 1 == type:
        url.addQueryItem('type', '1')
        url.addQueryItem('query', keyword)
        url.addQueryItem('page', '1')
    elif 2 == type:
        url.addQueryItem('type', '2')
        url.addQueryItem('query', keyword)
        url.addQueryItem('page', '2')
    # view.searchWxArticle('http://weixin.sogou.com/weixin?type=2&query=%E6%90%9E%E7%AC%91')
    # test 微信号
    # view.searchWxService(url)
    # view.parseWxNumberHome(QUrl('http://mp.weixin.qq.com/profile?src=3&timestamp=1477755435&ver=1&signature=GDDyd1Y3OVTxCrGuGZzQsertKX0LF9yULQwm0kn-rPXRb2dAerVWw06uawCkQqU4etpYmqWLmuKhjfW2QQw1qg=='))
    view.parseWxArticle(QUrl('http://mp.weixin.qq.com/s?timestamp=1477759661&src=3&ver=1&signature=ZYVg-oqTE86YJjL2ahRhJae54Yap4I5MAG7B3s*M5h9iG75B8vyjflchYvJgxfkqbmjT4dVJgGXx9Qf6OOefYfi3GeiY9SRRjlgdRf8tmm91MgjfAQmk5*pye-5ZkkOLo*kIEO724rsWk0i1wP1dvDUXNapv*bWZBO1VpHWNKic='))
    # view.page().userAgentForUrl = u'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
    # view.load(QUrl('http://mp.weixin.qq.com/s?timestamp=1477759661&src=3&ver=1&signature=ZYVg-oqTE86YJjL2ahRhJae54Yap4I5MAG7B3s*M5h9iG75B8vyjflchYvJgxfkqbmjT4dVJgGXx9Qf6OOefYfi3GeiY9SRRjlgdRf8tmm91MgjfAQmk5*pye-5ZkkOLo*kIEO724rsWk0i1wP1dvDUXNapv*bWZBO1VpHWNKic='))
    # 测试读取的结果
    html = '''
 
    
    '''
    # view.setHtml(html)
    view.show()
    app.exec_()
