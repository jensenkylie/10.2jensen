def cumsum(list):
     x = 0
     total = 0
     while x < len(list):
         total += list[x]
         print total
         x = x + 1
     return total

list = [1, 2, 4, 8, 16]
print cumsum(list)


