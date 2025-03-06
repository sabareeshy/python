index = 1
limit = 100
result = 0
sum = 0
square_sum = 0

while index <= limit:
    sum = sum + index
    square_sum = square_sum + (index * index)
    index +=1

sum_of_square = sum * sum
result = sum_of_square - square_sum
print(result)

