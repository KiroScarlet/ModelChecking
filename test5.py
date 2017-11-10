import itertools
import re
file_path=input("请输入文件所在位置：")
print(file_path)
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
f.close()


def Effect(act):
    f=open('/home/kiroscarlet/ModelChecking/machine.txt','r')#改成自己的文件夹
    for i in f.readlines():
        if re.findall("Effect\("+act, i):
            act_effect=re.findall('\[(.+?)\]', i)
            if len(act_effect)>0:
                return(act_effect[0])
    f.close()


for i in Act:
    print(Effect(i))
a=[]
print(len(a))