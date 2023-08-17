# create function
def print_vat(gross, vat_percentage=20, message='Summary:'):
    net = gross/(1 + (vat_percentage/100))
    vat = gross - net
    print(message, 'net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))


def print_vat_named_params(*, gross, vat_percentage=20, message='Summary:'):
    net = gross/(1 + (vat_percentage/100))
    vat = gross - net
    print(message, 'net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))


# call the function
print_vat(9.99, 20, 'Price Breakdown:')
print_vat(24.99, 15, "Summary:")
print_vat(1)
print_vat(8.5, message='Breakdown:')
print_vat(8.5, message='Breakdown:', vat_percentage=10)

# print_vat_named_params(13, 22) this doesn't work!
print_vat_named_params(gross=15, vat_percentage=22)
print(1, 2, 'three', True, ":")
print(1, 2, 'three', True, sep=":")

