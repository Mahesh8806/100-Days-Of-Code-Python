def add(*args):
    print(args)
    print(args[0])
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6))


# Key word arguments...

def calculate(n, **kwargs):
    print(kwargs)

calculate(23, name="Mahesh",surname="Bunage")