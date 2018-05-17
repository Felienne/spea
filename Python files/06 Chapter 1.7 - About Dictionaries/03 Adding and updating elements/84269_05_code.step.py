# 
Explore updating a dictionary.

babel_fish = {1: 'uno', 2: 'dos', 3: 'tres'}
babel_fish.update({1: __})
babel_fish.update({2: __})
babel_fish.update({__:'tres'})
assertEqual(babel_fish, {1: 'een', 2: 'twee', 3: 'drie'})