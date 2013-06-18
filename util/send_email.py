#!/usr/bin/env python
# -*- coding: gb18030 -*-

import sys
import time
import smtplib
from email.mime.text import MIMEText


#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.163.com"
mail_user="news_recommend"
mail_pass="web_new"
mail_postfix="163.com"

def send_mail(to_list,subject,content):
    '''
    to_list:发给谁
    subject:主题
    content:内容
    send_mail("aaa@126.com","subject","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content, 'html', 'gb18030')
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,gb18030,utf-8"
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

def load_recommend_news(input_filename):
    userid_news_list_dict = dict()
    for line in open(input_filename):
        term_list = line.strip().split('\t')
        if len(term_list) != 4: continue
        user_id, url, title, reason = term_list
        if user_id not in userid_news_list_dict:
            userid_news_list_dict[user_id] = []
        userid_news_list_dict[user_id].append( (url, title, reason) )
    return userid_news_list_dict

def build_content(news_list):
    content = ''
    for news in news_list:
        content = content + '\t'.join(news) + '\n'
    return content

def build_html_content(name, news_list):
    html_content = '<p>Hi, %s<br>&nbsp&nbsp以下是根据你的兴趣定期为你推荐的新闻<br><br></p>' %(name)
    for url, title, reason in news_list:
        html_content = html_content + '<a href="' + url + '">' + title + '<font size="1">&nbsp' + reason + '</font>' + '</a><br><br>'

    html_content += '<p><br><b>来自网页搜索新产品组</b><br><br></p>'
    return html_content

def main():
    if len(sys.argv) != 2: 
        print>>sys.stderr, 'usage: python send_email.py filename'
        sys.exit(0)

    recommend_person_info_list = [(r'李文涛', '1648410941', '2A299833351005B3AF74A65E7CD3D4A9', 'liwentao@sogou-inc.com')]

    st = time.localtime()
    subject = '%s月%s日%s时新闻推荐' %(st.tm_mon, st.tm_mday, st.tm_hour)
    print>>sys.stderr, 'LOG:%02d%02d%02d' %(st.tm_mon, st.tm_mday, st.tm_hour)
    print>>sys.stderr, subject
    
    all_html_content = ''
    userid_news_list_dict = load_recommend_news(sys.argv[1])
    for recommend_person_info in recommend_person_info_list:
        name, weibo_id, yyid, email_address = recommend_person_info
        user_id = None
        news_list = None
        if yyid in userid_news_list_dict:
            news_list = userid_news_list_dict[yyid]
            user_id = yyid
        elif weibo_id in userid_news_list_dict:
            news_list = userid_news_list_dict[weibo_id]
            user_id = weibo_id
        if not news_list: continue
        html_content = build_html_content(name, news_list)
        all_html_content += html_content
        content = build_content(news_list)

        if send_mail([email_address], subject, html_content):
            print>>sys.stderr, user_id, '发送给%s成功' %(name)
        else:
            print>>sys.stderr, user_id, '发送给%s失败' %(name)
        print>>sys.stderr, content
        print>>sys.stderr

    email_address_list = [ 'liwentao@sogou-inc.com']
    for email_address in email_address_list:
        time.sleep(1)
        send_mail([email_address], subject, all_html_content)
    print>>sys.stderr
    print>>sys.stderr

if __name__ == '__main__':
    main()

