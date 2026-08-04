from functools import reduce

l=[2,7,9,5]
def sum(a,b):
    return a+b

result=reduce(sum,l)

print(result)