def print_params(a, b, c):
    print(a.upper(), b.lower(), c.capitalize())


print_params('dass', 'fwfa', 'fasdsa')

word = 'hello'
hobby = 'yoga'
name = 'bob'

print_params(word, hobby, name)

bob_values = word, hobby, name
dave_values = 'hi', 'golf', 'dave'
julie_values = ['hey', hobby, name]

# unpacking with asterisk!!
print_params(*bob_values)
print_params(*dave_values)
print_params(*julie_values)


firstname = 'victoria'
lastname = 'lloyd'

print(firstname, lastname)


def add(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result


print(add())
answer = add(2, 6, 11, 12, 44, 41, 2)
print(answer)

# two stars is for unpacking a dictionary
