# -*- encoding: utf-8 -*-

my_list = [ 1, 'a', None ]
my_dict = { 'a':'a value', 'b':'b value' }

args = ('string', u'üñîçø∂é string', 5 * 5,
       my_list, my_dict)

print '''
string : %s
unicode: %s
number : %d
list   : %s
dict   : %s
''' % args