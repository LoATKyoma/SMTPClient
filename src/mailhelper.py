import fire
import os
from sender import sender


class mailhelper:
    def login(self, user, password):
        '''
         登录指令\n
         param user 用户邮箱地址\n
         param password 邮箱授权码\n
        '''
        sender().login(True, user, password)

    def sendmails(self, mailList, subjectText, msgText):
        '''
        循环发送邮件\n
        param mailList 收件人列表，应为csv文件
        param subjetText 主题文件，为txt格式，里面包含邮件的主题
        param msgText 邮文，为txt格式，包含邮件的主要内容
        '''
        mailCore = sender()
        mailCore.login()
        # 判断输入的是否正确
        if not mailCore.isLogin():
            print('尚未绑定邮箱信息，请先使用login命令绑定邮箱信息')
            return
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
