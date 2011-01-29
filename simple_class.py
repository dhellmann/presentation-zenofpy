class MyClass(object):
    """Class documentation.
    """
    
    def __init__(self, arg1, arg2):
        self.attr1 = arg1
        self.attr2 = arg2
    
    def do_something(self):
        """Does some work and returns a value.
        """
        return self.attr1 * self.attr2

obj = MyClass(1, 2)
print obj.do_something()