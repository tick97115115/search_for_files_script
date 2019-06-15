#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, sys, multiprocessing

def main(path,name,logfile = 0):
    a = path.split(';')#如果要键入的目标路径为复数，则在目标路径之间用分隔符;分割
    b = a
    while len(a) != 0:
        c = a
        a = check_every_subfolders(c)
        for x in a:
            b.append(x)
    for t in b:
        filter_files(t,keyname)

def check_every_subfolders(path):
    l = []
    for x in path:
        try:
            os.chdir(x)
        except PermissionError as e:
            print('PermissionError:',e)
            continue
        else:
            a = [y for y in os.listdir(x) if os.path.isdir(y)]
        if len(a) == 0:
            continue
        else:
            for z in a:
                l.append(os.path.join(x,z))
    return l

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


if __name__ == "__main__":
    path = input('please enter aim path:')
    path = os.path.abspath(path)
    keyname = input('please enter the file`s name you want to find out:')
    main(path,keyname)