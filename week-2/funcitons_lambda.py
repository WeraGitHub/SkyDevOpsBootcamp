printoo = lambda a, b: print(a, b)
printoo('gello', 'grw')

compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)

x = 42
y = 300

print("a > b", compare(x, y))


numbers_list = [2, 4, 6, 8]

new_list = list(map(lambda z: z + 1, numbers_list))
print(new_list)

new_list = list(map(lambda z: z ** 2, numbers_list))
print(new_list)
