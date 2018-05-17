# Transposing is easy too, and works exactly how you would expect. <div>The command is:

</div><div><pre><code>numpy.transpose(matrix)</code></pre></div><div><div>
Use the transpose command, to print this matrix: </div><div>
</div><pre><pre><code>[[1 4 7]
 [2 5 8]
 [3 6 9]]</code></pre>
</pre>This of course is the transposed version of the matrix we created in the previous step.</div>
import numpy
list_1_to_9 = list(range(1,10))
matrix_1_to_9 = numpy.reshape(list_1_to_9, (3, 3))
transposed = ___(matrix_1_to_9)
print(transposed)