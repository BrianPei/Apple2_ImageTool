# coding:utf-8

import os
import tkMessageBox

def modify_time(date, time):
    result = os.system('adb shell date -s "'+date+'.'+time+'00"')
    if result == 0:
        print 'system time has been modified!'
    else:
        print 'modify time failed!'     

def push_file(path,folder_dict):
    os.system('adb remount')
    for (k,v) in folder_dict.items():
        source = path + '\\' + k
        result1 = os.system('adb push '+source+ ' ' +v)
        if result1 == 0:
            print '%s upload successful!'%k
        else:
            print '%s upload failed!'%k
        os.system('adb shell busybox find '+v+'/ -type f -exec touch {} \;')
    tkMessageBox.showinfo('message', '操作完成')
    
def root_device():
    os.system('adb root')