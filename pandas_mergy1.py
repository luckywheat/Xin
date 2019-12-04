import pandas as pd

allxls = []
filenums = int(input('请输入需要合并的文件个数：'))
for i in range(filenums):
    filename = input('请输入第' + str(i + 1) + '个文件名：') + '.xlsx'
    data = pd.read_excel(filename)
    allxls.append(data)

result_data = pd.concat(allxls, ignore_index=True)
print('正在写入文件。。。')
result_data.to_excel('result.xlsx')
print('数据保存完成')