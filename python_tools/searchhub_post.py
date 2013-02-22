#! /usr/bin/python
#encoding:gb18030

import urllib
import urllib2
import cookielib

def searchhub_post(post_url, params):
    '''ģ����searchhub����post��ʾ

    test_post()��Ϊһ�������Ƽ�����Ĳ�������
    '''

    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0')]
    urllib2.install_opener(opener)

    req = urllib2.Request(post_url, urllib.urlencode(params))
    req.add_header("Referer","http://gouwu.sogou.com")
    resp = urllib2.urlopen(req)
    data = resp.read()
    return data.decode('utf-16le', 'ignore')

def test_post():

    post_url = r"http://gouwu.sogou.com/api/"
    params = {"queryString":"http://item.taobao.com/item.htm?id=10022350070", "title":"Ԫ�ؼٷ� ���ɷ��� Ů�� �ٷ� �̷��� �̾� jiafa",
            "queryType":"recommendquery", "parity":"1358820965005213_scenerecognitionquery_recommendquery", "start":0, "end":4,
            "queryFrom":"shoppingext", "sceneType":"detail"}

    print searchhub_post(post_url, params).encode('gb18030')

if __name__ == '__main__':

    test_post()
