import sys
def add (num1, num2):
    add = num1 + num2
    return add

def sub (num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
   sum = add(num1, num2)
   print(sum)

if operation == "sub":
    subt = sub(num1, num2)
    print(subt)

if operation == "mul":
    mult = mul(num1, num2)
    print(mult)
