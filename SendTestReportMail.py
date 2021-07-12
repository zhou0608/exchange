# -*- coding : utf-8 -*-
from SendMailWithAtt import Mail
from ProjectVar import *
import  os
from GetConfigInfo import GetConfigInfo

#发送测试报告邮件
def send_test_report_mail(send_content):
    '''
    :param mail_host: 邮件服务器
    :param mail_user: 发件邮箱的用户名
    :param mail_passwd: 发件邮箱的授权码
    :param sender: 发件箱地址
    '''

    #创建GetConfigInfo实例，用于获取邮件配置信息,传入配置文件路径
    get_config_info = GetConfigInfo(mail_conf_file_path)

    #获取邮件服务器、邮箱用户、邮箱授权码、发件人地址
    mail_host = get_config_info.get_option_value("mail","Mail_Host")
    mail_user = get_config_info.get_option_value("mail","Mail_User")
    mail_passwd = get_config_info.get_option_value("mail","Mail_Passwd")
    sender = get_config_info.get_option_value("mail","Mail_Sender")

    #配置文件取出的是一个字符串不是列表，需要把字符串转为列表
    receiver = eval(get_config_info.get_option_value("mail","Mail_Receiver"))
    # print(mail_host,mail_user,mail_passwd,sender,type(receiver))
    #创建Mail实例
    mail = Mail(mail_host,mail_user,mail_passwd,sender)

    #发送测试报告
    mail.send_mail(receiver,"每日轮动策略购买",send_content)

if __name__ == "__main__":
    send_test_report_mail("126自动化测试报告")