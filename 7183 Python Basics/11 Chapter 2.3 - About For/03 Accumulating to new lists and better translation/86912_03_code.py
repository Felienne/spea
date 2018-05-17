# Remember that, if we want to get a nice sentence from the list, we can use ' '.join(list).<div>
</div><div>Now print the capitalized sentence "I Love Programming And Python Is Nice".
<div>
</div></div>
input = "I love programming and Python is nice"
output = [] #<-- we start with an empty list as result
words = input.split() 
for w in words:
   output.append(w.capitalize())
print(__)