ran = range(5, 20 + 1)

list_comprehension = [
    x
    for x in ran
    if x % 2 != 0
] 
print(list_comprehension)