# coding:utf-8

from Tkinter import *
from Tkconstants import *
import time
import config   
import transfer

#读取配置文件
conf = config.Config()
conf.read('config.ini')

#修改手机系统时间
def modify_time(Event):
    target_date = date_win.get()
    time_value = time_list.get(time_list.curselection())
    target_time = (time_value).replace(':','')
    transfer.modify_time(target_date, target_time)

#上传图片文件至手机相应目录
def excute_upload(Event):
    folder_dict = {}
    for x in folder_list.curselection():
        selected = folder_list.get(x)
        target = conf.get('target', (selected))
        folder_dict[selected]=target
    print folder_dict
    transfer.push_file(path, folder_dict)


def root(Event):
    transfer.root_device()

# 定义窗口
window = Tk(className='ImageTool')
window.geometry('640x480')

# 左侧列表
left_frame = Frame(window)
left_frame.pack(side=LEFT, padx=20, ipady=10)

time_label = Label(left_frame, text='TIME')
time_label.pack()
time_list = Listbox(left_frame, height=25, width=25,exportselection=False)
#获取配置文件中时间列表
times = conf.options('time')
for key in times:
    value = conf.get('time', key)
    time_list.insert(END,value)
time_list.pack()

# 中部区域
center_frame = Frame(window)
center_frame.pack(side=LEFT,ipady=20,padx=10)

path_frame = Frame(center_frame)
path_frame.pack(pady=20)
path_label = Label(path_frame,text='图片文件夹路径')
path_label.pack()
#获取配置文件中图片文件夹路径
path = conf.get('path', 'folder_path')
path_value = StringVar()
path_win = Entry(path_frame,width=20,textvariable=path_value,stat='readonly')
path_win.pack()
path_value.set(path)

date_frame = Frame(center_frame)
date_frame.pack(pady=20)
date_label = Label(date_frame,text='请输入日期(格式:yyyymmdd)')
date_label.pack()
time_value = StringVar()
date_win = Entry(date_frame,width=20,textvariable=time_value)
date_win.pack()
time_value.set(time.strftime('%Y%m%d',time.localtime(time.time())))
time_button = Button(date_frame, width=15, text='修改手机时间')
time_button.bind('<Button-1>', modify_time)
time_button.pack(pady=10)

run_button = Button(center_frame, width=15, text='运行')
run_button.bind('<Button-1>', excute_upload)
run_button.pack(pady=30)

tip_frame = Frame(center_frame)
tip_frame.pack(pady=30)
tip_label = Label(tip_frame,text='如果修改系统时间未生效,\n请点击下方按钮进行root后重试')
tip_label.pack()
root_button = Button(tip_frame,width=15,text='root')
root_button.bind('<Button-1>', root)
root_button.pack()

# 右侧列表
right_frame = Frame(window)
right_frame.pack(side=RIGHT,padx=20, ipady=10)

folder_label = Label(right_frame,text='FOLDER')
folder_label.pack()
folder_list = Listbox(right_frame,height=25,width=25,selectmode=MULTIPLE,exportselection=False)
folders = conf.options('target')
for folder in folders:
    folder_list.insert(END,folder)
folder_list.pack()

window.mainloop()
