a = 1
b = 2
c = 0
result = 2
limit = 10
while (a + b) < limit:
     c = a + b
     if c % 2 == 0:
       result = result + c
print(result)