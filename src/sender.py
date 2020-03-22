# -*- coding: utf-8 -*-
' sender module '

__author__ = 'yinghuiZhang'

import smtplib
import os
import csv
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


class sender:
    def __init__(self):
        '''
        好像没什么用的初始化函数
        '''
        self.mailUser = None
        self.mailPass = None
        self.mailHost = None

    def login(self, isChange=False, user=None, password=None):
        """
        录入用户信息\n
        param isChange 是否要更新登录信息，是则根据user与password更新info.user文件内容，否则根据info.user文件登录\n
        param user 你的邮箱地址\n
        param password 邮箱授权码
        """
        if not os.path.isfile('info.user'):
            file = open('info.user', mode='w', encoding='utf-8')
            file.close()
        if isChange:
            self.mailUser = user
            self.mailPass = password
            self.mailHost = 'smtp.' + self.mailUser[self.mailUser.find('@') +
                                                    1:]
            file = open('info.user', mode='w', encoding='utf-8')
            str = self.mailUser + ' ' + self.mailPass
            file.write(str)
            file.close()
        else:
            file = open('info.user', mode='r', encoding='utf-8')
            str = file.read()
            if len(str) > 0:
                self.mailUser = str[:str.find(' ')]
                self.mailPass = str[str.find(' ') + 1:]
                self.mailHost = 'smtp.' + self.mailUser[self.mailUser.
                                                        find('@') + 1:]

    def sendMail(self, tarUser, title, textMsg, ext=[], senderName=''):
        '''
        单发邮件给指定用户地址\n
        param tarUser 指定用户的地址\n
        param title 邮件的主题\n
        param textMsg 正文的文件路径\n
        param ext 附件列表，默认为空\n
        param senderName 自定义发送者名字
        '''
        # 添加正文
        message = MIMEMultipart()
        message['From'] = senderName + '<%s>' % self.mailUser
        message['To'] = tarUser
        message['Subject'] = title
        textMsgSubType = mimetypes.guess_type(textMsg)[0].split('/')[-1]
        if textMsgSubType is None:
            print('无法识别的文件类型')
            return
        with open(textMsg, 'rb') as file:
            mainPart = MIMEText(file.read(), textMsgSubType, _charset='utf-8')
            message.attach(mainPart)

        # 根据附件列表添加附件
        for extPart in ext:
            if isinstance(extPart, str):
                kind = mimetypes.guess_type(extPart)[0]
                if kind is None:
                    continue
                if kind.split('/')[0] == 'image':
                    with open(extPart, 'rb') as file:
                        img = MIMEImage(file.read(),
                                        _subtype=kind.split('/')[-1])
                        img['Content-Type'] = 'application/octet-stream'
                        img['Content-Disposition'] = \
                            'attachment;filename="%s"' % extPart
                        message.attach(img)
                elif kind.split('/')[0] == 'text':
                    with open(extPart, 'rb') as file:
                        content = file.read()
                        text = MIMEText(content,
                                        _subtype=kind.split('/')[-1],
                                        _charset='utf-8')
                        text['Content-Type'] = 'application/octet-stream'
                        text['Content-Disposition'] = \
                            'attachment;filename="%s"' % extPart
                        message.attach(text)
                elif kind.split('/')[0] == 'application':
                    with open(extPart, 'rb') as file:
                        app = MIMEApplication(file.read(),
                                              _subtype=kind.split('/')[-1])
                        app['Content-Type'] = 'application/octet-stream'
                        app['Content-Disposition'] = \
                            'attachment;filename="%s"' % extPart
                        message.attach(app)
                else:
                    print('无法识别的文件内容')
        try:
            # 发送邮件
            smtp = smtplib.SMTP()
            smtp.connect(self.mailHost, 25)
            smtp.login(self.mailUser, self.mailPass)
            smtp.sendmail(self.mailUser, tarUser, message.as_string())
            smtp.quit()
        except smtplib.SMTPException as e:
            print('error', e)

    def isLogin(self):
        '''
        检查是否已经有了登录信息
        '''
        if self.mailUser is not None and \
            self.mailPass is not None and \
                self.mailHost is not None:
            return True
        else:
            return False

    def sendMails(self, tarUserList, title, textMsg, ext=[], senderName=''):
        '''
        根据发送名单循环单发邮件\n
        param tarUserList 目标用户的名单，csv文件\n
        param title 邮件的主题或包含邮件主题的txt文件\n
        param textMsg 正文的文件路径\n
        param ext 附件列表，默认为空\n
        param senderName 自定义发送者名字
        '''
        # 读取目标群体
        nameList = []
        with open(tarUserList, 'r') as csvFile:
            spamReader = csv.reader(csvFile)
            for row in spamReader:
                for column in row:
                    nameList.append(column)
        # 判断是不是文件
        if os.path.isfile(title):
            with open(title, 'r', encoding='utf-8') as titleFile:
                subject = titleFile.read()
        else:
            subject = title
        # 循环发送
        for tarUser in nameList:
            self.sendMail(tarUser, subject, textMsg, ext, senderName)
