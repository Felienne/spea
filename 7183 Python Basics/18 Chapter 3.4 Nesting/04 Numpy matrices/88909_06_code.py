# 
Explore a nice way to create the matrix:


<pre><code>[[1 2 3]
 [4 5 6]
 [7 8 9]]</code></pre> 


In line 2 we create a list from 1 to 9, you should know how to do that!
Then in line 3 we 'reshape' this list into the form we want. Can you guess the arguments needed there?

import numpy
list_1_to_9 = list(range(__,__))
matrix_1_to_9 = numpy.reshape(list_1_to_9, (__, __))
print(matrix_1_to_9)