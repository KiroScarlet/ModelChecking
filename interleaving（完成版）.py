import itertools
import re
import os
def read(f):#用正则匹配截取左右大括号中的内容，以逗号为间隔分割成列表
    return re.findall(r"{(.+?)}",f.readline())[0].split(",")

def effect_read(f,Effect):#读取Effect函数，并以行数组的形式保存下来
    while True:
        line = f.readline()
        if line =='':
            break
        Effect.append(line)
    Effect[-1]=Effect[-1][:-3]

f=open(input("请输入文件1："),'r')#对文件1进行读取

Loc1=read(f)
Loc01=read(f)
Var1=read(f)#Var用来存储变量名
var1=Var1[:]#var用来存储每个变量的取值范围
for i in range(len(var1)):
    var1[i]=read(f)
for i in range(len(var1)):
    for j in range(len(var1[i])):
        var1[i][j] = int(var1[i][j])

Act1=read(f)
g01=read(f)

t1=[]#t数组是一个状态转换的四元组
f.readline()
while True:
    line=f.readline()
    if re.findall("Effect", line):
        break
    t1.append(re.findall("\((.+?)\)",line)[0].split(","))

Effect1=[]
effect_read(f,Effect1)

f.close()

f=open(input("请输入文件2："),'r')#对文件2进行读取

Loc2=read(f)
Loc02=read(f)
Var2=read(f)
var2=Var2[:]
for i in range(len(var2)):
    var2[i]=read(f)
for i in range(len(var2)):
    for j in range(len(var2[i])):
        var2[i][j] = int(var2[i][j])
Act2=read(f)
g02=read(f)

t2=[]#t数组是一个状态转换的四元组
f.readline()
while True:
    line=f.readline()
    if re.findall("Effect", line):
        break
    t2.append(re.findall("\((.+?)\)",line)[0].split(","))
Effect2=[]
effect_read(f,Effect2)
f.close()


def Cartesian(list1,list2):#对两个列表进行笛卡尔积，返回合并之后的列表
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

def varMerge(Var,Var1,Var2,var,var1,var2):#对变量合并，相同变量只保留一个
    i=j=0
    while i<len(Var1) and j<len(Var2):
        Var.append(Var1[i])
        var.append(var1[i])
        if Var1[i]!= Var2[j]:
            Var.append(Var2[j])
            var.append(var2[j])
        i=i+1
        j=j+1

def transtationMerge(t,t1,t2):#合并转移关系
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





f=open('/home/kiroscarlet/ModelChecking/test2.txt','w')#对两个程序并行操作后，写入新的文件

Loc=Cartesian(Loc1,Loc2)
f.write('Loc=')
write_list(Loc,f)#写入Loc行

Loc0=Cartesian(Loc01,Loc02)
f.write('Loc0=')
write_list(Loc0,f)

Var=[]
var=[]
varMerge(Var,Var1,Var2,var,var1,var2)
f.write('Var=')
write_list(Var,f)#写入变量名

for i in range(len(Var)):#写入每个变量的取值范围
    f.write(Var[i]+'=')
    write_list(var[i],f)

Act=Act1+Act2
f.write('Act=')
write_list(Act,f)

g0=[]
g0.append('('+g01[0]+')'+' and '+'('+g02[0]+')')
f.write('g0=')
write_list(g0,f)

f.write('Translation\n')
t=[]
transtationMerge(t,t1,t2)
for i in t:
    f.write(r'    (')
    for j in i[0:-1]:
        f.write(str(j)+',')
    f.write(str(i[-1])+')\n')
f.write('Effect\n')

Effect=Effect1+Effect2
for i in Effect:
    f.write(i)



import itertools
import re
#file_input=input("请输入文件：")
f=open('/home/kiroscarlet/ModelChecking/test2.txt','r')#改成自己的文件夹
Loc=read(f)
# 用正则匹配截取左右大括号中的内容，以逗号为间隔分割成列表
print(Loc)

Loc0=read(f)
print(Loc0)

Var=read(f)
print(Var)
var=Var[:]
print(var)
for i in range(len(var)):
    var[i]=read(f)

for i in range(len(var)):
    for j in range(len(var[i])):
        var[i][j] = int(var[i][j])
print(var)
print(Var)
Act=read(f)
print(Act)

g0=read(f)
print(g0)

t=[]#t数组是一个状态转换的四元组
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
    f = open('/home/kiroscarlet/ModelChecking/test2.txt', 'r')
    for i in f.readlines():
        if re.findall("Effect\("+act, i):
            act_effect = re.findall('\[(.+?)\]', i)
            if act_effect:
                return(act_effect[0])
            else:
                return 'True'
    f.close()

s = list(itertools.product(Loc, *var))  #状态s是loc和所有变量的笛卡尔积

f=open('/home/kiroscarlet/ModelChecking/test2.dot','w')
f.write('digraph G { \n')
result=[]#此列表用来存储结果
node=set()#此集合用来存储可达的结点
for i in s:
    for j in s:
        for k in t:

            n=0
            for l in Var:#对每一个变量赋值
                exec(l+'=i[n+1]')
                n=n+1

            if i[0] == k[0] and j[0] == k[3] and eval(k[1]):
                exec(Effect(k[2]))
                is_var=['']
                is_var[0]=j[0]
                for l in Var:
                    exec('is_var.append('+l+')')
                if is_var==list(j):
                    result.append([i,j,k[2],0])#暂时以四元祖的形式存储下来

                    n = 0
                    for l in Var:
                        exec(l + '=i[n+1]')
                        n = n + 1

                    if eval(g0[0]) and i[0] == Loc0[0]:
                        node.add(i) #把初始状态添加到可达结点集合中
                        f.write("%s_%d[peripheries=2]\n" % (i[0], i[1]))#输出初始状态，两个圈表示节点是初始状态

while True:
    n=0
    for i in result:
        if (i[0] in node) and i[3]==0:#把可达状态关联的边的状态位标记为1
            i[3]=1
            n=n+1
            node.add(i[1])
    if n==0:
        break

for i in result:
    if i[3]==1:#状态位为一表示此边关联结点是可达的
        f.write('%s_%d->%s_%d[label="%s"]\n' % (i[0][0], i[0][1], i[1][0], i[1][1], i[2]))


f.write('}')
f.close()
