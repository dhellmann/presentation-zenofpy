def gen_values(n):
    for i in range(n):
        yield i*i

print gen_values(5)

for i in gen_values(5):
    print i