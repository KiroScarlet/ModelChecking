import itertools
import re

f=open('/home/kiroscarlet/ModelChecking/machine.txt','r')#改成自己的文件夹
Loc=re.findall(r"{(.+?)}",f.readline())[0].split(",")
# 用正则匹配截取左右大括号中的内容，以逗号为间隔分割成列表
print(Loc)

Loc0=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Loc0)

Var=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Var)
var=Var[:]
print(var)
for i in range(len(var)):
    var[i]=re.findall(r"{(.+?)}",f.readline())[0].split(",")

for i in range(len(var)):
    for j in range(len(var[i])):
        var[i][j] = int(var[i][j])
print(var)
print(Var)
Act=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Act)

g0=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(g0)

t=[]
#t数组是一个状态转换的四元组
f.readline()
while True:
    line=f.readline()
    if re.findall("Effect", line):
        break
    t.append(re.findall("\((.+?)\)",line)[0].split(","))
f.close()
print(t)

#对于每一个Action，检索对应的对变量的操作后返回
def Effect(act):
    f = open('/home/kiroscarlet/ModelChecking/machine.txt', 'r')  # 改成自己的文件夹
    for i in f.readlines():
        if re.findall("Effect\("+act, i):
            act_effect = re.findall('\[(.+?)\]', i)
            if act_effect:
                return(act_effect[0])
            else:
                return 'True'
    f.close()
print(Effect(Act[5]))