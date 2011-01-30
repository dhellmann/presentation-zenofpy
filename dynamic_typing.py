class A(object):
    def do_something(self):
        print 'in A'

class B(object):
    def do_something(self):
        print 'in B'

def work_on_obj(c):
    c.do_something()

a = A()
b = B()

work_on_obj(a)
work_on_obj(b)