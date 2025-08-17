
# ----- этот вариант в одну строку, но не все такое любят, поэтому варианта решения два -----

print(max([len(word) for word in input()[:-1].split() if 'Y' not in word]))


