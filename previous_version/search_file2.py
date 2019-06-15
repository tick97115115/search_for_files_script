#/usr/bin/python3
# -*- coding: UTF-8 -*-

__auther__ = "wang"
###################
import os
###################
#此脚本是添加了模糊匹配功能的文件搜索脚本：可以键入文件名的其中一段关键字去打印出文件名相匹配的文件绝对路径
###################
def filter_files(path,keyname):
    os.chdir(path)
    l = len(keyname)
    a = [x for x in os.listdir('.') if os.path.isfile(x)]
    for x in a:
        n = 0
        m = len(x) - l
        if m < 0:
            continue
        elif m == 0:
            if keyname == x:
                print(os.path.join(path,x))
            else:
                continue
        else:
            for y in x:
                if n > m:
                    continue
                if y == keyname[0]:
                    if keyname == x[n:n+l]:
                        print(os.path.join(path,x))
                n = n + 1

            #print(os.path.join(b,x))

def recursion_directories(path):#输入一个含有目标路径的列表，输出目标路径的下所有的子目录绝对路径
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