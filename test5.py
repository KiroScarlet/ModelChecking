def make_name():
    names = locals()
    for i in range(1, 10):
        names['t%s' % i] = i
        print (names['t%s' % i])
make_name()