# 
In lines 1 and 2 we define a function that looks like it doubles in input. But....! There is no return line, so the function will not return anything.

That is were <code>None</code> comes in.

See what happens when we assign the result of no_return_double_function(5) to a variable.

def no_return_double(n):
    a = n + n
what_am_I = no_return_double(5)
assertEqual(__, what_am_I)