# 
Updating dictionaries can be done by assigning to elements, just like in lists.

babel_fish = {1: 'uno', 2: 'dos', 3: 'tres'}
babel_fish[1] = __
babel_fish[2] = __
babel_fish[__] = 'drie'
babel_fish[__] = __
assertEqual(babel_fish, {1: 'een', 2: 'twee', 3: 'drie', 4: 'vier'})