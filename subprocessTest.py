import subprocess

ret = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#执行命令dir，并将结果放到PIPE中
print('stdout: ',ret.stdout.read().decode('gbk'))
print('stderror: ',ret.stderr.read().decode('gbk'))

