file_write_handle = open('file_fruit.txt', 'w')

file_write_handle.write('Apple\n')
file_write_handle.write('Banana\n')

list_of_fruit = ['Cherries\n', 'Damson\n', 'Fig\n']

file_write_handle.writelines(list_of_fruit)