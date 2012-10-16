#coding=utf8
from django.db import models
from django.contrib.auth.models import User
# Create your models herea.
class User_contact(models.Model):
	user = models.ForeignKey(User)
	phone = models.CharField(max_length = 15)
	contact = models.CharField(max_length = 20)

import email
import string,time

class MailCreator:
    def __init__(self):
        # 创建邮件的message对象
        self.msg = email.Message.Message()
        self.mail = ""    
        
    def create(self, mailheader, maildata):
        # mailheader 是dict类型，maildata是list, 且里面第一项为纯文本类型，第二项为html.
        # mailattachlist 是list, 里面为附件文件名
        if not mailheader or not maildata:
            return
        
        for k in mailheader.keys():
            # 对subject要作特殊处理，中文要转换一下。
            # 比如 "我的一个测试邮件" 就要转换为 =?gb2312?b?ztK1xNK7uPay4srU08q8/g==?=
            if k == 'subject':
                self.msg[k] = email.Header.Header(mailheader[k], 'utf-8')           
            else:
                self.msg[k] = mailheader[k]
        # 创建纯文本部分
        body_plain = email.MIMEText.MIMEText(maildata[0], _subtype='plain', _charset='utf-8')
        body_html = None
        # 创建html部分，这个是可选的
        if maildata[1]:
            body_html = email.MIMEText.MIMEText(maildata[1], _subtype='html', _charset='utf-8')
        
        
        # 创建一个multipart, 然后把前面的文本部分和html部分都附加到上面，至于为什么，可以看看mime相关内容
        attach=email.MIMEMultipart.MIMEMultipart()
        attach.attach(body_plain)
        if body_html:
            attach.attach(body_html)
        # 生成最终的邮件            
        self.mail = self.msg.as_string()[:-1] + attach.as_string()
        
        return self.mail

