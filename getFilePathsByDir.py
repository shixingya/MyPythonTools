# -*- coding: utf-8 -*-
'''
�����Ŀ¼·�����ݹ齫Ŀ¼�¼���Ŀ¼���ļ����浽�ļ���
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
            '''print('�ļ��У�%s'%tmp_path)'''
            traverse(tmp_path)
            

 
path = raw_input("���������Ŀ¼��eg:D:/2014Files��: ");
print "���������Ŀ¼Ϊ : ", path
fileName = raw_input("�����ļ�·���洢·����eg:D:/2014.txt��: ");
print "�����ļ�·���洢·��Ϊ : ", fileName
traverse(path) 