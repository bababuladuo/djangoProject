import os
import xlrd2 #xlrd: 对Excel进行读相关操作
# import xlwt #xlwt: 对Excel进行写相关操作，且只能创建一个全新的Excel然后进行写入和保存。
# import numpy
# import matplotlib
# from prettytable import PrettyTable  #PrettyTable 是python中的一个第三方库，可用来生成美观的ASCII格式的表格
# from matplotlib import pyplot as plt
file_path='D:/box/djangoProject/blog/service/data'
#导入文件
def get_files_name():
    """
    用于获取文件名
    :return:返回值为文件名组成的列表
    """
    file_list = os.listdir(file_path)#填写文件路径
    return file_list

#保存生产Excel表
def load_data(file_list):
    """
    用于读取指定的文件并保存至字典数据结构中
    :param file_list: 需要加载的文件列表
    :return: 保存了文件内容的字典
    """
    item_list=[]

    for file in file_list:
        #获取表格文件
        book = xlrd2.open_workbook(file_path+'/'+file)
        #获取表格中的所有sheet
        names = book.sheet_names()
        #获取第一个sheet
        sheet = book.sheet_by_index(0)
        #获取当前表格的行数
        rows = sheet.nrows
        #获取当前表格的列数
        cols = sheet.ncols
        #获取表头文件，即表格第一行
        head = sheet.row_values(0)
        for row in range(rows-1):
            #如果当前字典中没有则创建一个
            dictionary = {}
            item_list.append(dictionary)
            for col in range(cols-1):
                content=sheet.cell_value(row+1,col+1)
                if content=="":
                    continue
                dictionary[head[col+1]] =sheet.cell_value(row+1,col+1)
    return item_list

mapper={
    "长":"length",
    "宽":"width",
    "高":"height",
    "品名":"name",
    "包装类别":"way",
    "件数":"num",
    "单件毛重":"weight"
}

def service():
    res = load_data(get_files_name())
    mapper_res=[]
    for item in res:
        new_item={}
        for attr in item:
            for m in mapper:
                if m in attr:
                    new_item[mapper[m]] = item[attr]
        mapper_res.append(new_item)
    return mapper_res

if __name__ == '__main__':
    for item in service():
        print(item)


