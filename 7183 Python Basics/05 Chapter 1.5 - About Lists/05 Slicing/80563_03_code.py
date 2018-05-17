# Try to figure our the right answers to these <i>slices</i>.
dutch = ['nul', 'een', 'twee', 'drie', 'vier', 'vijf']
greater_than_three = dutch[4:6]
assertEqual(greater_than_three, __)

also_greater_than_three = dutch[4:100]
assertEqual(also_greater_than_three, __)

less_than_four = dutch[0:4]
assertEqual(less_than_four, __)

hoedje_van_papier = dutch[__:__]
assertEqual(hoedje_van_papier, ['een', 'twee', 'drie', 'vier'])