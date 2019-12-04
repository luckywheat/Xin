# import sys

source_data = []
used_data = []

f = open('65w.txt','r')
for line in f.readlines():
    line = line.strip()
    if not len(line) or line.startswith('#'): 
        continue
    source_data.append(line)
print('原始资源共有%s条' % len(source_data))
f.close()

f = open('ok.txt','r')
for line in f.readlines():
    line = line.strip()
    if not len(line) or line.startswith('#'): 
        continue
    used_data.append(line)
print('已使用资源%s条' % len(used_data))
f.close()

filted_data = list(set(source_data) - set(used_data))
print('未使用资源%s条' % len(filted_data))
f = open('filted_data.txt','w')
for i in range(len(filted_data)):
    f.write(str(filted_data[i])+'\n')
f.close()
