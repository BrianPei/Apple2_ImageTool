# coding:utf-8

import ConfigParser

#重写ConfigParser的option方法以区分大小写
class Config(ConfigParser.ConfigParser):
    def optionxform(self, option):
        return option