import re

testy = 'The quick brown fox jumps over the lazy dog'

m = re.search(r"(quick|slow).*(fox|camel)", testy)

if m:
    print('Matched', m.groups())
    print('Starting at', m.start())
    print('Ending at', m.end())


################## regex substitutions

test_string = 'Perl for Perl Programmers'
# sub or subn

new_string, number = re.subn('Perl', 'Python', test_string)
if number:
    print(new_string)
    print(number)

new_string2 = re.sub('Perl', 'Python', test_string)
if number:
    print(new_string2)


################## regex splits

line = 'root:;0.0:superuser,/root;/bin/sh'
elements = line.split(':')
print(elements)

elements2 = re.split('[:;.,]', line)
print(elements2)


################## regex findall  -  finditer

test_string = '/dev/sd3d 135398 69683 52176 57% /home/stuff'

numbers = re.findall(r'\b\d+\b', test_string)
print(numbers)

for match in re.finditer(r'\b(\d+)\b', test_string):
    print(match.groups())
