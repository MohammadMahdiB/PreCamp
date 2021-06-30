j = 0
for i in range(123, 568):
    if i % 5 == 0 or i % 6 == 0:
        j+=i
print(j)