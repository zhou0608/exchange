# -*- coding : utf-8 -*-
'''
根据配置ini的配置文件内容
获取对应option的内容
'''
import  configparser
class GetConfigInfo(object):

    def __init__(self,config_path):
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    #获取section下option的值
    def get_option_value(self,section_name,option_name):
        return self.cf.get(section_name,option_name)


    #获取所有的section
    def get_all_section(self):
        return self.cf.sections()

    #获取某section下的所有option
    def get_all_option(self,section_name):
        return  self.cf.options(section_name)

    #获取section下所有option的键值对
    def get_section_items(self,section_name):
        items = self.cf.items(section_name)
        #把option的选项名和值作为键值对返回
        return dict(items)

if __name__ == "__main__":
    from ProjectVar import *
    g = GetConfigInfo(mail_conf_file_path)
    print(g.get_all_section())
    print(g.get_all_option("mail"))
    print(g.get_option_value("mail","Mail_Host"))
    print(g.get_section_items("mail"))





