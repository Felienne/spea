# 

<div>We want to use the nested loops to print the cards in order of value, so:
7 of Clubs</div><div>7 of Diamonds
7 of Hearts</div><div>7 of Spades</div><div>8 of Clubs </div><div>...

How should we change the code?</div><div>
</div>



suits = ['clubs', 'diamonds', 'hearts', 'spades']
values = ['7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
for suit in suits:
    for value in values:
        print(value + ' of ' + suit.capitalize())