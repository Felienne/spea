# 
If you created the dictionary like me, you just included the elements needed for the calculation 2 + 2 = 4


<pre><code>calculations_to_letters = {'2':'two', '+': 'plus', '=':'equals', '4':'four'}</code></pre>


Other letters are not needed anyway! But now, the program will try a few more secret calculations. You cannot see them, but they will be tried with your code. All numbers will be below 10.

For all these secret calculations, your program needs to return the right words, so the dictionary must contain more elements.

calculations_to_letters = {'2':'two', '+': 'plus', '=':'equals', '4':'four'}
input = input() #<--here the secret calculations are read
calculation_elements = input.split()
element_1 = calculation_elements[0]
word_1 = calculations_to_letters[element_1]

element_2 = calculation_elements[1]
word_2 = calculations_to_letters[element_2]

element_3 = calculation_elements[2]
word_3 = calculations_to_letters[element_3]

element_4 = calculation_elements[3]
word_4 = calculations_to_letters[element_4]

element_5 = calculation_elements[4]
word_5 = calculations_to_letters[element_5]

output = word_1 + ' ' + word_2 + ' ' + word_3 + ' ' + word_4 + ' ' + word_5

print(output) #<-- the output is printed and compared to the secret answers