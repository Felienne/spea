# 
babel_fish = {1: 'uno', 2: 'dos', 3: 'tres'}
two_in_spanish = babel_fish.get(2, 'Key not found in the dictionary')
assertEqual(__,two_in_spanish)
four_in_spanish = babel_fish.get(4, 'Key not found in the dictionary') 
assertEqual(__,four_in_spanish)