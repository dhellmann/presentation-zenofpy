def outer(arg):
    print 'outer(%s)' % arg
    
    def inner(val):
        print 'inner(%s) (arg=%s)' % (val, arg)
        return val * arg

    return inner

print 'Creating thrice:'
thrice = outer(3)

print '\nCalling thrice:'
print thrice(3)
print thrice('a')