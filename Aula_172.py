l1 = [1, 2, 3, 4, 5, 6, 7, 8]

l2 = [1, 2, 3, 4, 5]

l3 = []

for i in range(len(l1)):
    for j in range(len(l2)):
        if i == j:
            l3.append(l1[i]+l2[j])

print(l3)