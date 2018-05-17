# 
The 3x3 identity matrices are not complete. Run the code to see how they print, and then complete them.

identity_basic = [[1, 0, 0], [0, 1, 0]]
print("I am I3 in normal Python {0}".format(identity_basic))

import numpy
identity_numpy = numpy.matrix('1 0 0; 0 1 0')
print("I am I3 in NumPy  {0}".format(identity_numpy))