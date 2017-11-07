import itertools

loc = ['start', 'select']
loc0 = ['start']
nsoda = [0, 1, 2]
nbeer = [0, 1, 2]
var = [nsoda, nbeer]

act = ['bget', 'sget', 'coin', 'ret_coin', 'refill']
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

s = list(itertools.product(loc, *var))  # 状态s是loc和所有变量的笛卡尔积

f=open('/home/kiroscarlet/桌面/test111.dot','w')
f.write('digraph G { \n')

for i in s:
    for j in s:
        for k in t:
            nsoda=i[1]
            nbeer=i[2]

            if i[0] == k[0] and j[0] == k[3] and eval(k[1]):
                m, n = effect(k[2], i[1], i[2])
                if m == j[1] and n == j[2]:
                    print('%s%d%d->%s%d%d[label="%s"]' % (i[0], i[1], i[2], j[0], j[1], j[2], k[2]))
                    f.write('%s%d%d->%s%d%d[label="%s"]' % (i[0], i[1], i[2], j[0], j[1], j[2], k[2]))
                    f.write('\n')
                    if eval(g0[0]) and i[0] == loc0[0]:
                        print("%s%d%d[peripheries=2]" % (i[0], i[1], i[2]))  #两个圈表示节点是初始状态
                        f.write("%s%d%d[peripheries=2]" % (i[0], i[1], i[2]))
                        f.write('\n')
f.write('}')
f.close()