s = ' string value '

print 'split     : %r' % s.split()
print 'strip     : %r' % s.strip()
print 'substring :', 'str' in s

s2 = s.strip()
print 'startswith:', s2.startswith('s')
print 'endswith  :', s2.endswith('end')

print 'join      :', ':'.join(['a', 'b', 'c'])