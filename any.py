#coding:utf-8
__author__ = 'xjt'

def test():

    a = 1
    def test1():
        global a
        a = 2
    test1()
    print(a)

a = 3
test()
#print (a)
