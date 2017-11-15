import itertools
import re
#file_input=input("请输入文件：")
f=open('/home/kiroscarlet/ModelChecking/test2.txt','r')#改成自己的文件夹
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