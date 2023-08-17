numbers = [42, 66, 12, 3, 99, 3.142, 42]

print(f"Minimum: {min(numbers)}, maximum {max(numbers)}")

print(sum(numbers))

names_ages = {'fred': 3, 'jim': 8, 'dave': 42}

# dictionaries implement min, max and sum on the KEYS
print(f"Minimum: {min(names_ages)}, maximum {max(names_ages)}")

print(f"Minimum: {min(names_ages.values())}, maximum {max(names_ages.values())}")

# tuple operations
a = 6
b = 20
print(a, b)
print(f"a: {a}, b: {b}")
a, b = b, a
print(f"a: {a}, b: {b}")


gouda, edam, caithness = range(3)
print(edam)
print(gouda)
print(caithness)
