
# ----- развернутый и более понятный вариант кода из файла 2.1 -----

line = input()[:-1].split()
all_len = []

for word in line:
    if 'Y' not in word:
        all_len.append(len(word))

print(max(all_len))

