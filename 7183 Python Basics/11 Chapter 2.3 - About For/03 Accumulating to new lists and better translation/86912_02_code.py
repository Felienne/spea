# <p class="wysiwyg-text-align-left">Translate all words in the sentence "I love programming and Python is very nice"  to uppercase and print the result, by starting with an empty list and appending translated elements to the resulting list.

input = "I love programming and Python is nice"
output = [] #<-- we start with an empty list as result
words = input.split() 
for w in words:
   output.__(w.capitalize())
print(output)