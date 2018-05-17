# <div>We now create infinity directly, rather than as a result of a calculation. For this we import the math module of which it is part.

</div><div><pre><code>import math
test = math.inf</code></pre></div><div>
</div>Verify that these rules hold for infinity in Python:


<li>infinity/x = infinity, for any x</li><li>x/infinity = 0, for any x</li><li>infinity * x = infinity, for any x</li>


import math
infinity = math.inf
assertEqual(infinity, infinity / __)
assertEqual(__, 12/infinity)
assertEqual(__, infinity * 12)