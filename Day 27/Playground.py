from numpy.ma.core import multiply


def add(*args):
    sum=0
    for arg in args:
        sum += arg
    return sum

print(add(1,2,3,4,5))

def calculate(n,**kwargs):
    for key, value in kwargs.items():
        print(key, value)

        n+=kwargs["add"]

        return n

print(calculate(2,add=5,multiply=3))

