import pandas as pd

allxls = []
filenums = int(input('请输入需要合并的文件个数：'))
iris_concat = pd.DataFrame()
for filenum in range(filenums):
    filename = input('请输入第' + str(filenum + 1) + '个文件名：') + '.xlsx'
    allxls.append(filename)

    iris = pd.read_excel(filename, None)
    keys = list(iris.keys())
    
    for i in keys:
        iris1 = iris[i]
        iris_concat = pd.concat([iris_concat, iris1], ignore_index=True)
    
    print('已读取')


iris_concat.to_excel('ok.xlsx')