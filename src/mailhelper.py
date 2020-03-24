# -*- coding: utf-8 -*-

import fire
import os
from sender import sender


class mailhelper:

    def setuser(self, user, password):
        '''
         设置用户信息指令\n
         param user 用户邮箱地址\n
         param password 邮箱授权码/密码，根据邮箱的要求决定
        '''
        sender().setUserInfo(user, password)

    def setsmtp(self, address, port):
        '''
         设置smtp服务器指令\n
         param address 用户邮箱地址\n
         param port 邮箱授权码\n
        '''
        sender().setSMTPServer(address, port)

    def sendmails(self, mailList, subjectText, msgText):
        '''
        循环发送邮件\n
        param mailList 收件人列表，应为csv文件
        param subjetText 主题文件，为txt格式，里面包含邮件的主题
        param msgText 邮文，为txt格式，包含邮件的主要内容
        '''
        mailCore = sender()
        userRet = mailCore.getUserInfo()
        smtpRet = mailCore.getSMTPServer()
        # 判断输入的是否正确
        if not userRet:
            print('用户信息不完善，请用setuser命令设置用户信息')
            return
        elif not smtpRet:
            print('smtp服务器信息不完善，请用setsmtp命令设置smtp服务器及其端口信息')
        if not os.path.exists(mailList):
            print('发送名单路径不存在')
            return
        if not os.path.exists(subjectText):
            print('主题文件路径不存在')
            return
        if not os.path.exists(msgText):
            print('邮件正文文件路径不存在')
            return
        mailCore.sendMails(mailList, subjectText, msgText)


def main():
    fire.Fire(mailhelper())


if __name__ == '__main__':
    main()
