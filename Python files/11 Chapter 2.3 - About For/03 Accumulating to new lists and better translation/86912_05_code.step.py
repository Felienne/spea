# For reference, here is the original code:<div>
</div><div><pre><code>calculations_to_letters = {'2':'two', '+': 'plus', '=':'equals', '4':'four'}
input = "2 + 2 = 4"

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

print(output)</code></pre> 
</div><div>Can you do it with just 10 lines?</div>
calculations_to_letters = {'2':'two', '+': 'plus', '=':'equals', '4':'four'}
input = "2 + 2 = 4"

calculation_elements = input.split()
output = __
for i in __:
    word = calculations_to_letters[__]
    __ #<-- do something with word here.

print(output)