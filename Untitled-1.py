import xlrd
#import pymysql
from datetime import datetime
from xlrd import xldate_as_tuple

data = xlrd.open_workbook("H:\匠准数控机床\机床数据\TP640终检表.xls")   #读取D盘中名为sales_data的excel表格
table_one = data.sheet_by_index(0)           #根据sheet索引获取sheet的内容
#table_two = data.sheet_by_index(1)

for i in range(0, table_one.nrows):
    row = table_one.row(i)
    for j in range(0, table_one.ncols):
        print(table_one.cell_value(i, j), "\t", end="")
    print()