import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print 'Found    :', match.re.pattern
print 'In       :', match.string
print 'Range    :', s, '-', e
print 'Substring:', text[s:e]