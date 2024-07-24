#Map function and filter function

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: "even" if x % 2 == 0 else "odd", L)))  # this is using map function, taking L a list as a paramter and returning even or odd

print(list(filter(lambda x: x > 2, [1,2,3,4,5])))