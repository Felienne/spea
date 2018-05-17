# 
Try to figure our the right answers to these <i>slices</i>.


measurements = [-6, -2, 0, 2, 6]
negative_values = measurements[:2]
assertEqual(negative_values, __)

postive_values = measurements[__:]
assertEqual(postive_values, [2, 6])

zero_and_above = measurements[__]
assertEqual(zero_and_above, [0, 2, 6])

last_element = measurements[4:]
assertEqual(last_element, __)

first_element = measurements[:__]
assertEqual(first_element, [-6])