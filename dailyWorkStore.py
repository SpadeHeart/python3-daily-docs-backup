import sys
path='D:\\ideproject\\pycharmproject\\demo1'
sys.path.append(path)

import datetime
import os
import shutil

today = datetime.date.today()
path1 = "C:\\Users\\spade\\Desktop\\临时工作文件"
path2 = "E:\\工作文档"
subDirName = today.strftime("%Y-%m-%d")
des_dir = os.path.join(path2,subDirName)

files=[]
filenames=[]

oldDesFiles=[]

# 用于获取源目录现有文件
def fn(path):
    #key = dict()
    for i in os.listdir(path):
        filenames.append(i)
        sub_path = os.path.join(path, i)
        if os.path.isdir(sub_path):  # 递归遍历子目录下文件及目录
            fn(sub_path)
        elif os.path.isfile(sub_path):  # 读取目录下文件
            # 读取目标文件名字
            files.append(sub_path)

# 用于获取目标目录现有文件
def fn2(path):
    #key = dict()
    for i in os.listdir(path):
        sub_path = os.path.join(path, i)
        if os.path.isdir(sub_path):  # 递归遍历子目录下文件及目录
            fn(sub_path)
        elif os.path.isfile(sub_path):  # 读取目录下文件
            # 读取目标文件名字
            oldDesFiles.append(sub_path)

def Oper():

    #清空目标文件夹现有文件
    for file in oldDesFiles:
        if not file in files:
            os.remove(file)

    #复制文件
    for file in filenames:
        # file是文件名
        source_path = os.path.join(path1,file)
        des_path = os.path.join(des_dir,file)
        shutil.copy(source_path,des_path)




if __name__ == "__main__":
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)
    fn(path1)
    fn2(des_dir)
    Oper()
    print("done!")
