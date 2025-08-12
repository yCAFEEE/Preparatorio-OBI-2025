str1 = input()
str2 = input()

cord_str1 = -1
cord_str2 = -1
for i_idx, i in enumerate(str1):
    for j_idx, j in enumerate(str2):
        if i == j:
            cord_str1 = i_idx + 1
            cord_str2 = j_idx + 1

print(cord_str1, cord_str2)