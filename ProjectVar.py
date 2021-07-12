#coding:utf8
'''
Author:Zhoujianjun
File:ProjectVar.py
Creatime:2021/4/2215:57
'''
import os

#当前项目路径
project_path = os.path.dirname(os.path.dirname(__file__))

#邮件配置文件地址
mail_conf_file_path = os.path.join(project_path,'exchange', "MailInfo.ini")

if __name__ == '__main__':
    print(project_path)
    print(mail_conf_file_path)