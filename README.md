
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
  将python文件打包成[mailhelper压缩包](./src/dist/mailhelper-0.1.1.tar.gz),可以将其下载后安装使用。该命令行工具包含三个命令，在首次使用的时候需要先设置用户和smtp服务器：
  * **setuser**  
  用于设置用户信息，包含两个参数，用户地址和邮箱授权码/密码，这个根据不同邮箱有不同的要求，比如说QQ邮箱就需要开启第三方授权并使用授权码，而hotmail则只需要设置好smtp服务器，使用邮箱密码即可。
  
  ```python
  mailhelper setuser xxxx@163.com password
  ```
  
  * **setsmtp**
  用于设置smtp服务器信息，包含两个参数，smtp服务器域名和使用的端口号

  ```python
  mailhelper setsmtp smtp.xxx.xxx 587
  ```

  * **sendmails**  
  用于发送邮件，包含三个参数,目标用户列表(.csv)，主题信息文件(.txt)，正文文件(.txt)

  ```python
  mailhelper sendmails maillist.csv subject.txt msg.txt
  ```

  * **使用范例**
    * 第一次使用

    ```python
    mailhelper setuser yourmail@hotmail.com password
    mailhelper setsmtp smtp.office365.com 587
    mailsendmails maillist.csv subject.txt msg.txt
    ```

    * 以后的使用，假如不需要变更邮箱和smtp服务器则直接发送邮件即可

    ```python
    mailsendmails maillist.csv subject.txt msg.txt
    ```
>
* **版本**  
  稍微可靠的测试版本0.1.1
>
* **其他**  
  里面还包含了图形界面发送邮件的源码，需要者可以自行更改[setup.py](./src/setup.py)重新打包
