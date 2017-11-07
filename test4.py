import itertools

loc = ['l1']
loc0 = ['l1']
x=[1,2,3,4,5,6,7,8,9]
var = [x]
act = ['x=2*x']
g0=['x=3']
def effect(act, x):
    if act == 'x=2*x':
        return 2*x

t = [['l1', 'True', 'x=2*x', 'l2']]

s = list(itertools.product(loc, *var))  #状态s是loc和所有变量的笛卡尔积

