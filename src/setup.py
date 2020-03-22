from setuptools import setup

setup(name="mailhelper",
      version="0.1.0",
      keywords=['mailhelper', 'sendmails'],
      description='A simple SMTP helper for sending mails for others',
      license='MIT license',
      url='https://github.com/LoATKyoma/SMTPClient',
      author='YinghuiZhang',
      author_email='yinghuizhang66@163.com',
      py_modules=['sender', 'mailhelper'],
      platforms='any',
      install_requires=[
          'fire',
          'setuptools',
      ],
      entry_points={'console_scripts': ['mailhelper = mailhelper:main']})
