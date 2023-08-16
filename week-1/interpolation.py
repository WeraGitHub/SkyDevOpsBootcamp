# Alex and Weronika

names = ['Tom', 'Harry', 'Jane', 'Mary']
suffix = ['st', 'nd', 'rd', 'th']
n = 1

for n, name in enumerate(names):
    s = f"{str(n+1) + suffix[n]} of {len(names)} is {names[n]}"
    print(s)


# iterate over
for index, (name, suffix) in enumerate(zip(names, suffix), start=1):
    s = f"{str(index) + suffix} of {len(name)} is {name}"
    print(s)