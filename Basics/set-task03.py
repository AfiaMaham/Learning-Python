# Filter Common Elements From Multiple Sets
# Find elements common to three sets.

set1 = {1, 3, 5, 7, 9}
set2 = {1, 2, 3, 4, 5}
set3 = {3, 6, 9}

set4 = set1.intersection(set2)
set4 = set4.intersection(set3)
print(set4)