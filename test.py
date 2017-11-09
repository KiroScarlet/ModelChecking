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
f.close()



def effect(act, nsoda, nbeer):
    if act == 'coin':
        return nsoda, nbeer
    if act == 'ret_coin':
        return nsoda, nbeer
    if act == 'sget':
        return nsoda - 1, nbeer
    if act == 'bget':
        return nsoda, nbeer - 1
    if act == 'refill':
        return 2, 2


t = [['select', 'nsoda>0', 'sget', 'start'],
     ['select', 'nbeer>0', 'bget', 'start'],
     ['select', 'nsoda==0 and nbeer==0', 'ret_coin', 'start'],
     ['start', 'True', 'coin', 'select'],
     ['start', 'True', 'refill', 'start']]

s = list(itertools.product(Loc, *var))  # 状态s是loc和所有变量的笛卡尔积
print(s)

f=open('/home/kiroscarlet/ModelChecking/test.dot','w')
f.write('digraph G { \n')

for i in s:
    for j in s:
        for k in t:
            n=0
            for l in Var:
                exec(l+'=i[n+1]')
                n=n+1
            if i[0] == k[0] and j[0] == k[3] and eval(k[1]):
                m, n = effect(k[2], i[1],i[2])
                if m == j[1] and n == j[2]:
                    print('%s%d%d->%s%d%d[label="%s"]' % (i[0], i[1], i[2], j[0], j[1], j[2], k[2]))
                    f.write('%s%d%d->%s%d%d[label="%s"]' % (i[0], i[1], i[2], j[0], j[1], j[2], k[2]))
                    f.write('\n')
                    if eval(g0[0]) and i[0] == Loc0[0]:
                        print("%s%d%sd[peripheries=2]" % (i[0], i[1], i[2]))  #两个圈表示节点是初始状态
                        f.write("%s%d%d[peripheries=2]" % (i[0], i[1], i[2]))
                        f.write('\n')
f.write('}')
f.close()