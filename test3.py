import itertools
import re

def read_file(f):
    return re.findall(r"{(.+?)}",f.readline())[0].split(",")
f=open(input("请输入文件1："),'r')#改成自己的文件夹
Loc1=re.findall(r"{(.+?)}",f.readline())[0].split(",")
# 用正则匹配截取左右大括号中的内容，以逗号为间隔分割成列表
print(Loc1)

Loc01=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Loc01)

Var1=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Var1)
var1=Var1[:]
print(var1)
for i in range(len(var1)):
    var1[i]=re.findall(r"{(.+?)}",f.readline())[0].split(",")

for i in range(len(var1)):
    for j in range(len(var1[i])):
        var1[i][j] = int(var1[i][j])
print(var1)
print(Var1)
Act1=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Act1)

g01=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(g01)

t1=[]
#t数组是一个状态转换的四元组
f.readline()
while True:
    line=f.readline()
    if re.findall("Effect", line):
        break
    t1.append(re.findall("\((.+?)\)",line)[0].split(","))

def effectRead(f,Effect):
    while True:
        line = f.readline()
        if line =='':
            break
        Effect.append(line)
    Effect[-1]=Effect[-1][:-3]
Effect1=[]
effectRead(f,Effect1)
print(Effect1)
f.close()
print(t1)

f=open(input("请输入文件2："),'r')#改成自己的文件夹
Loc2=re.findall(r"{(.+?)}",f.readline())[0].split(",")
# 用正则匹配截取左右大括号中的内容，以逗号为间隔分割成列表
print(Loc2)

Loc02=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Loc02)

Var2=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Var2)
var2=Var2[:]
print(var2)
for i in range(len(var2)):
    var2[i]=re.findall(r"{(.+?)}",f.readline())[0].split(",")

for i in range(len(var2)):
    for j in range(len(var2[i])):
        var2[i][j] = int(var2[i][j])
print(var2)
print(Var2)
Act2=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(Act2)

g02=re.findall(r"{(.+?)}",f.readline())[0].split(",")
print(g02)

t2=[]
#t数组是一个状态转换的四元组
f.readline()
while True:
    line=f.readline()
    if re.findall("Effect", line):
        break
    t2.append(re.findall("\((.+?)\)",line)[0].split(","))
Effect2=[]
effectRead(f,Effect2)
print(Effect2)
f.close()
print(t2)

def Cartesian(list1,list2):
    list=[]
    for i in list1:
        for j in list2:
            list.append(i+'_'+j)
    return list
def write_list(list,f):
    f.write('{')
    for i in list[0:-1]:
        j=str(i)
        f.write(j+',')
    f.write(str(list[-1])+'}\n')



Loc=Cartesian(Loc1,Loc2)
print(Loc)

Loc0=Cartesian(Loc01,Loc02)
print(Loc0)

f=open('/home/kiroscarlet/ModelChecking/test2.txt','w')
f.write('Loc=')
write_list(Loc,f)

f.write('Loc0=')
write_list(Loc0,f)


def varMerge(Var,Var1,Var2,var,var1,var2):
    i=j=0
    while i<len(Var1) and j<len(Var2):
        Var.append(Var1[i])
        var.append(var1[i])
        if Var1[i]!= Var2[j]:
            Var.append(Var2[j])
            var.append(var2[j])
        i=i+1
        j=j+1

Var=[]
var=[]
varMerge(Var,Var1,Var2,var,var1,var2)
print(var)
f.write('Var=')
write_list(Var,f)

for i in range(len(Var)):
    f.write(Var[i]+'=')
    write_list(var[i],f)
print(var)

Act=Act1+Act2
print(Act)
f.write('Act=')
write_list(Act,f)

g0=[]
g0.append('('+g01[0]+')'+' and '+'('+g02[0]+')')
f.write('g0=')
write_list(g0,f)
f.write('Translation\n')
t=[]
def transtationMerge(t,t1,t2):
    for i in t1:
        for j in t2:
            temp=i[:]
            temp[0]=i[0]+'_'+j[0]
            temp[3]=i[3]+'_'+j[0]
            t.append(temp)
    for i in t2:
        for j in t1:
            temp = i[:]
            temp[0] = j[0] + '_' + i[0]
            temp[3] = j[0] + '_' + i[3]
            t.append(temp)
t=[]
transtationMerge(t,t1,t2)

print(t)
for i in t:
    f.write(r'    (')
    for j in i[0:-1]:
        f.write(str(j)+',')
    f.write(str(i[-1])+')\n')

f.write('Effect\n')

Effect=Effect1+Effect2
print(Effect)
for i in Effect:
    f.write(i)
