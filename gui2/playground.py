# Multiple arguments / Multiple positional arguments
def add(*args):
    return sum(args)

print(add(1,2,3))


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['mul']
    print(n)
    
    
calculate(2, add=3, mul=5)