import itertools

Loc = ['start', 'select']
Loc0 = ['start']
var = [[0,1,2],[0,1,2]]
Var=['nsoda','nbeer']
Act = ['bget', 'sget', 'coin', 'ret_coin', 'refill']
g0 = ['nsoda==2 and nbeer==2']


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