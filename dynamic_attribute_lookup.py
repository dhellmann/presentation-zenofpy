class MyClass(object):
    
    CLASS_ATTR = 'class value'
    
    def __init__(self, arg):
        self.attr = arg

o = MyClass('instance value')
print o.attr
print o.CLASS_ATTR