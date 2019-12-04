import os
import random
import string
import shutil

print('本软件实现功能为将指定目录下的所有子目录中的二维码文件全部复制，')
print('粘贴到指定目录的all文件夹下，并生成随机文件名打乱顺序，以方便分')
print('码需要，使用前请将文件夹下所有的压缩包解压并删除压缩包，确保只有')
print('二维码文件')
print('=' * 30)
path = input('请粘贴文件夹的完整路径：')
target_path = path + '\\all'
os.makedirs(target_path)
g = os.walk(path)

file_names = []

for path, dir_list, file_list in g:
    for file_name in file_list:
        file_names.append(os.path.join(path, file_name))

random.shuffle(file_names)
count = 0
for file_name in file_names:
    path = os.path.dirname(file_name)
    new_path = file_name.replace(path, target_path)
    basename = os.path.basename(new_path)
    extname = os.path.splitext(new_path)
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    new_path = new_path.replace(basename, salt) + extname[1]
    print('%s已复制完成' % new_path)

    shutil.copy(file_name, new_path)
    count += 1

print('=' * 30)
print('共完成%s个文件的复制' % count)
