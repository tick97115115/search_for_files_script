#/usr/bin/python3
# -*- coding: UTF-8 -*-

__auther__ = "wang"
###################
import os
###################
#此脚本是搜索文件的脚本，通过键入查找文件的目标路径+目标文件的全名，之后打印出文件的绝对路径
###################
def filter_files(path,keyname):
    os.chdir(path)
    a = [r for r in os.listdir(path) if os.path.isfile(r)]
    b = os.path.abspath(path)
    for x in a:
        if x == keyname:
            print(os.path.join(b,x))

def recursion_directories(path):#输入一个含有目标路径的列表，输出所有目标路径的下的子目录绝对路径
    l = []
    for x in path:
        os.chdir(x)
        a = [y for y in os.listdir(x) if os.path.isdir(y)]
        if len(a) == 0:
            continue
        else:
            for z in a:
                l.append(os.path.join(x,z))
    return l

def method_zero(path,keyname):
    a = [path]
    b = a
    while len(a) != 0:
        c = a
        a = recursion_directories(c)
        for x in a:
            b.append(x)
    for t in b:
        filter_files(t,keyname)


if __name__ == "__main__":
    path = input('please enter aim path:')
    path = os.path.abspath(path)
    keyname = input('please enter the file`s name you want to find out:')
    method_zero(path,keyname)