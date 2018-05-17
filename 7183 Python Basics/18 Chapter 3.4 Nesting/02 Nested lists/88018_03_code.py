# 
How to get element from a nested list? And how to get elements from elements of nested lists?

beatles = ['John', 'Ringo', 'George', 'Paul']
one_direction = ['Niall', 'Liam', 'Harry', 'Louis']
traveling_wilburys = ['Bob', 'George', 'Jeff', 'Roy', 'Tom']

bands_I_like = [beatles, one_direction, traveling_wilburys]
assertEqual(__, bands_I_like[0])
assertEqual(__, bands_I_like[0][0])
assertEqual(__, bands_I_like[1])
assertEqual(__, bands_I_like[2][4])