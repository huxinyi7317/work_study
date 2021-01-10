import xlrd


def read_tab(tab_index,row,col,filepath = r'D:\pytest_test\jk_test\api_test\数据文件.xlsx'):
    #filepath表的路径，row行，col列,tab_index表索引
    work = xlrd.open_workbook(filepath)
    tb = work.sheet_by_index(tab_index)#选择表
    data = tb.cell(row,col)#读取单元格数据
    yield str(data)


for a in read_tab(0,1,1):
    print(a)