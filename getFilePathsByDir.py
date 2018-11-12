# -*- coding: utf-8 -*-
'''
输入根目录路径，递归将目录下及子目录下文件保存到文件中
'''
import os 
import sys


def traverse(fpth):
    fs = os.listdir(fpth)
    for f1 in fs:
        tmp_path = os.path.join(fpth,f1)
        if os.path.isfile(tmp_path):           
			wdj = open(fileName,'a+')			
			wdj.write(tmp_path)
			wdj.write("\n") 
			print(tmp_path)
        else:
            '''print('文件夹：%s'%tmp_path)'''
            traverse(tmp_path)
            

 
path = raw_input("输入遍历根目录（eg:D:/2014Files）: ");
print "输入遍历根目录为 : ", path
fileName = raw_input("输入文件路径存储路径（eg:D:/2014.txt）: ");
print "输入文件路径存储路径为 : ", fileName
traverse(path) 