# 
Print all points between and including (-5,-5) and (5,5), ordered by the x coordinate. 

So:

(-5, -5)
(-5, -4)
(-5, -3)
(-5, -2)
(-5, -1)
(-5, 0)
(-5, 1)
(-5, 2)
etc...

for x in range(-5,5):
    for y in range(-5,5):
        print(x,y)