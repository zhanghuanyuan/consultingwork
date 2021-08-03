"""
@author: JANG Hwan-won

name:create files

excel要求
1、excel表格要不加表头的，放在第一列上
2、excel表格读取默认sheet
3、不要有重复值

运行要求
1、根据需要修改path和file_path参数

"""
import os
import pandas as pd 
#读取excel路径
path='C:\\Users\\liurong\\Desktop\\工作簿2.xlsx'
#输出的文件夹路径
file_path=os.path.abspath(r'C:\\Users\\liurong\\Desktop\\test')

data=pd.read_excel(path,header = None,sheet_name = 0)
for indexs in data.index:
	name=data.loc[indexs].values[0]
	file_name=file_path + "\\"+name
	os.makedirs(file_name)

