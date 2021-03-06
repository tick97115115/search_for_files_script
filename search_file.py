#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, sys

def main(path,name,logfile = 0):
    a = [path]
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
            a = [y for y in os.listdir(x) if os.path.isdir(y)]
        except PermissionError as e:
            print('PermissionError:',e)
            continue
        if len(a) == 0:
            continue
        else:
            for z in a:
                l.append(os.path.join(x,z))
    return l

def filter_files(path,keyname):
    try:
        os.chdir(path)
        l = len(keyname)
        a = [x for x in os.listdir('.') if os.path.isfile(x)]
    except PermissionError as e:
        print('PermissionError:',e)
    else:
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
    path = input('please press target path:\n')
    path = os.path.abspath(path)
    keyname = input('please press the name of the file you want to find out:\n')
    main(path,keyname)