# coding=utf-8
import os
######### 将文件夹下文件统一改名############
#将文件当前后缀current_suffix改为modify_suffix, append为false时,后缀名替换,否则拼接在原后最名后
def rename_file(current_dir, current_suffix, modify_suffix, append):
    # listdir：返回指定的文件夹包含的文件或文件夹的名字的列表
    files = os.listdir(current_dir)
    for file in files:
        fileName = current_dir + os.sep + file
        # 运用递归;isdir：判断某一路径是否为目录
        if os.path.isdir(fileName):
            rename_file(fileName, current_suffix, modify_suffix, append)
            continue
        else:
            if file.endswith(current_suffix):
                if append == False:
                    modify_name = file.replace(current_suffix, modify_suffix)
                    print("修改前:" + current_dir + os.sep + file)
                    print("修改后:" + current_dir + os.sep + modify_name)
                    os.renames(current_dir + os.sep + file,
                               current_dir + os.sep + modify_name)


if __name__ == '__main__':
    print("task end ==----------------------------------------------------------------")
    rename_file("E:\\SAP\\面试资源2.3\\04 四大BI需求之四BW项目相关\\宋提供BW电网相关资料\\电网相关资料",
                ".doctt", ".doc", False)
    print("task end ==----------------------------------------------------------------")
