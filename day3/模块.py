'''import sys
#print(sys.path)#打印环境变量
print(sys.argv)'''

import os
#cmd_res = os.system("dir")#执行命令，不保存结果
cmd_res = os.popen("dir").read()
print(cmd_res)

os.mkdir("new_dir")#当前文件夹下创建新的文件夹