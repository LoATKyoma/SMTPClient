
# 简单的SMTP邮件发送工具实现

* **实现功能**

  根据提供的名单，主题，和正文，可以根据名单列表进行循环单发（实际上是群发，但是看起来像是一封封邮件发给别人）
>
* **依赖**
  * python标准库

    * smtplib

    * email

    * mimetypes

    * csv

    * os

    * tkinter
  
  * 第三方库

    * [fire](https://github.com/google/python-fire)

    * setuptools
>
* **命令行工具**
  将python文件打包成[mailhelper压缩包](./dist/mailhelper-0.1.0.tar.gz),可以将其下载后安装使用。该命令行工具包含两个功能，在第一次使用前需要先用login功能登记信息：
  * **login**
  用于登记或修改用户信息，包含两个参数，用户地址和邮箱授权码
  
  ```python
  mailhelper login xxxx@163.com
  ```

  * **sendmails**
  用于发送邮件，包含三个参数,目标用户列表(.csv)，主题信息文件(.txt)，正文文件(.txt)

  ```python
  mailhelper sendmails maillist.csv subject.txt msg.txt
  ```
>
* **版本**
  及其不靠谱的测试版本0.1.0
>
* **其他**
  里面还包含了图形界面发送邮件的源码，需要者可以自行更改[setup.py](./src/setup.py)重新打包
