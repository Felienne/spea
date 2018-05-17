# Try to figure our the right answers to these <i>slices</i>.
colors = ['Black', 'White', 'Grey', 'Green', 'Pink']
grayscale = colors[0:3]
assertEqual(grayscale, __)

colors_with_g = colors[2:__]
assertEqual(colors_with_g, ['Grey', 'Green'])

nothing = colors[4:0]
assertEqual(nothing, __)