# Alex and Weronika

# create variables, one integer and one string
num = 42
txt = '3'

# compare string that was cast to integer with integer
if int(txt) < num:
    # if it's True print WOW
    print('Wow')
else:
    # otherwise print Doh...
    print('Doh')

# compare string that was cast to float with integer
if float(txt) < num:
    # if it's True print WOW
    print('Wow')
else:
    # otherwise print Doh...
    print('Doh')

# if we turn num to string and then compare two strings together...it still works
num = '42'
if txt < num:
    print('Wow')
else:
    print('Doh')
