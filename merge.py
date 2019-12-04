# -*- coding: utf-8 -*-

# 将多个Excel文件合并成一个
import xlrd
import xlsxwriter

# 打开一个excel文件


def open_xls(file):
    fh = xlrd.open_workbook(file)
    return fh

# 获取excel中所有的sheet表


def getsheet(fh):
    return fh.sheets()

# 获取sheet表的行数


def getnrows(fh, sheet):
    table = fh.sheets()[sheet]
    return table.nrows

# 读取文件内容并返回行内容


def getFilect(file, shnum):
    fh = open_xls(file)
    table = fh.sheets()[shnum]
    num = table.nrows
    for row in range(num):
        rdata = table.row_values(row)
        datavalue.append(rdata)
    return datavalue

# 获取sheet表的个数


def getshnum(fh):
    x = 0
    sh = getsheet(fh)
    for sheet in sh:
        x += 1
    return x


if __name__ == '__main__':
    # 定义要合并的excel文件列表
    allxls = []
    i = int(input('请输入文件的个数：'))
    for filename in range(i):
        filename = input('请输入文件名：') + '.xlsx'
        allxls.append(filename)

    # 存储所有读取的结果
    datavalue = []
    for fl in allxls:
        fh = open_xls(fl)
        x = getshnum(fh)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum + 1)+"个sheet表的内容...")
            rvalue = getFilect(fl, shnum)
    # 定义最终合并后生成的新文件
    endfile = input('请输入合并后的文件名：') + '.xlsx'
    wb1 = xlsxwriter.Workbook(endfile)
    # 创建一个sheet工作对象
    ws = wb1.add_worksheet('拉群订单')
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c = rvalue[a][b]
            ws.write(a, b, c)
    wb1.close()
    print("文件合并完成")
