# 
Run the code with is and verify that this indeed works. In later lessons we will explain exactly what the differences between == and is are, but for now just remember that with None, it is better to use is.

babel_fish = {1: 'uno', 2: 'dos', 3: 'tres'}
four_in_spanish = babel_fish.get(4) #<-- contains None
if four_in_spanish is None:  #<-- when we are checking if something is None we use is and not ==!
    result = four_in_spanish
else:
    result = 'The key was not found'

assertEqual(__, result)