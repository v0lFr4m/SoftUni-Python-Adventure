from functools import reduce
def sum_nums(*args):
    return sum(args)

def sub_nums(*args):
    return reduce(lambda x,y: x-y, args)

def multiply(*args):
    return reduce(lambda x,y: x*y, args)

def divide(*args):
    return reduce(lambda x,y: x/y, args )

mapper = {
    '+': sum_nums,
    '-': sub_nums,
    '*': multiply,
    '/': divide
}
def operate(sign,*args):
    func = mapper[sign]
    return func(*args)

print(operate("+", 1, 2, 3))