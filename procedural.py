def my_function(arg1, arg2):
    """This function multiplies arg1 by arg2.
    """
    return arg1 * arg2

results = []
for i in range(5):
    results.append(my_function(i, i))

print results