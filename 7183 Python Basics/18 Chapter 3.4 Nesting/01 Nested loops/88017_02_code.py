# 
Some things are wrong with the nested loop. Can you fix it?

suits = ['clubs', 'diamonds', 'hearts', 'spades']
values = ['7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
for suit in suits:
    for value in values:
    print(value + ' of ' + suit.capitalize())