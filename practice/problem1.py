index = 1
limit = 1000
result = 0
while index < limit:
   if (index % 3 == 0) or (index % 5 == 0):
      result = result + index
   index += 1
print (result)
   
