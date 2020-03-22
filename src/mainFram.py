# -*- coding: utf-8 -*-
'主窗口界面'

import csv
import tkinter as tk
from tkinter import filedialog
from sender import sender


class Application(tk.Frame):
    def __init__(self, master=None):
        if master is not None:
            screenwidth = master.winfo_screenwidth()
            screenheight = master.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (300, 120, (screenwidth - 320) / 2,
                                        (screenheight - 200) / 2)
            master.geometry(alignstr)
            master.update()
        super().__init__(master)
        self.mailCore = sender()
        self.mailCore.login()
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # 选择发送名单
        self.tarUserList = tk.Label(self.master, text='发送给:')
        self.tarUserList.grid(row=0, column=0)
        self.tarUserList.update()
        self.tarUserListPath = tk.Label(self.master,
                                        text='',
                                        bg='white',
                                        width=self.master.winfo_width() -
                                        self.tarUserList.winfo_width() - 225)
        self.tarUserListPath.grid(row=0, column=1, columnspan=2)
        self.addUserList = tk.Button(self.master,
                                     text='...',
                                     command=lambda: self._onOpenFileDown_(
                                         self.tarUserListPath, 0, False))
        self.addUserList.grid(row=0, column=3)

        # 设定主题
        self.subject = tk.Label(self.master, text='主题:')
        self.subject.grid(row=1, column=0)
        self.subjectEntry = tk.Entry(self.master,
                                     width=self.master.winfo_width() -
                                     self.tarUserList.winfo_width() - 225)
        self.subjectEntry.grid(row=1, column=1, columnspan=2)

        # 选择发送的邮件文本
        self.mainTextMsg = tk.Label(self.master, text='邮件文本:')
        self.mainTextMsg.grid(row=2, column=0)
        self.mainTextMsg.update()
        self.mainTextPath = tk.Label(self.master,
                                     text='',
                                     bg='white',
                                     width=self.master.winfo_width() -
                                     self.tarUserList.winfo_width() - 225)
        self.mainTextPath.grid(row=2, column=1, columnspan=2)
        self.addUserList = tk.Button(
            self.master,
            text='...',
            command=lambda: self._onOpenFileDown_(self.mainTextPath, 1, False))
        self.addUserList.grid(row=2, column=3)

        # 选择附件 -todo

        # 发送与绑定账号
        self.mailConfig = tk.Button(
            self.master,
            text='设置',
            command=lambda: self._onConfigButtonDown_())
        self.mailConfig.grid(row=3, rowspan=2, column=0, columnspan=2)
        self.sendMail = tk.Button(
            self.master,
            text='发送',
            command=lambda: self._onSendMailButtonDown_())
        self.sendMail.grid(row=3, rowspan=2, column=2, columnspan=2)

    def _createLoginLevel_(self):
        loginLevel = tk.Toplevel(master=self.master)
        loginLevel.title('绑定邮箱信息')
        loginLevel.grab_set()
        userLabel = tk.Label(loginLevel, text='邮箱地址')
        userLabel.grid(row=0, column=0)
        passwordLabel = tk.Label(loginLevel, text='授权码')
        passwordLabel.grid(row=1, column=0)
        userEntry = tk.Entry(loginLevel, show=None)
        userEntry.grid(row=0, column=1)
        passwordEntry = tk.Entry(loginLevel, show=None)
        passwordEntry.grid(row=1, column=1)
        confirmBotton = tk.Button(
            loginLevel,
            text='确定',
            command=lambda: self._onLoginConfirmDown_(
                loginLevel, userEntry.get(), passwordEntry.get()))
        confirmBotton.grid(row=2, column=0)

    def _onLoginConfirmDown_(self, weight, user, passw):
        self.mailCore.login(True, user, passw)
        weight.destroy()

    def _onOpenFileDown_(self, comment, bottonIndex, openList):
        if not openList:
            if bottonIndex == 0:
                filePath = filedialog.askopenfilename(filetypes=[('CSV',
                                                                  '.csv')])
            elif bottonIndex == 1:
                filePath = filedialog.askopenfilename(
                    filetypes=[('文本文档', '.txt'), ('html文本', '.html')])
            comment['text'] = filePath
        else:
            # todo
            pass

    def _onConfigButtonDown_(self):
        self._createLoginLevel_()

    def _onSendMailButtonDown_(self):
        # 读取目标群体
        nameList = []
        with open(self.tarUserListPath['text'], 'r') as csvFile:
            spamReader = csv.reader(csvFile)
            for row in spamReader:
                for column in row:
                    nameList.append(column)
        # 读取主题
        mailSubject = self.subjectEntry.get()
        print(mailSubject)
        # 读取邮报
        mailText = self.mainTextPath['text']
        # 循环发送邮报
        for tarUser in nameList:
            self.mailCore.sendMail(tarUser, mailSubject, mailText)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
