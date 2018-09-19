# -*- coding: utf-8 -*-

#openFiles.py
#Create by Akihiro Yamada on 2018/09/19.
#Copyright (c) 2018. All Rights Reserved.


#開くファイル名(絶対パス)を記述したテキストファイルを
#読み込み、記述されているファイルを開く。
#ファイルの書式
#---------------
#ファイル名
#ファイル名
#....
#---------------

import os
import subprocess

fileName = "fileNames.txt"
f = open(fileName)

#開くファイルのファイル名を一つずつ読み込む
for line in f:
    if line == "":
        continue
    #行末の改行文字を切り離す。
    openFileName = line.splitlines()
    if os.name == 'nt':
        subprocess.Popen(['start', openFileName[0]], shell=True)
    elif os.name == 'posix':
        subprocess.Popen(['open', openFileName[0]])