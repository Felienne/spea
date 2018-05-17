# Explore what happens when you remove the index before or after the colon (:)
temperatures_this_week = [21, 20, 18, 19, 20, 20, 10]
temperatures_weekend = temperatures_this_week[5:]
assertEqual(temperatures_weekend, __)

temperatures_weekdays = temperatures_this_week[:5]
assert(temperatures_weekdays == __)