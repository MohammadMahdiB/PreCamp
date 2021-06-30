i: int
for i in range(200, 19,-1):
    if i % 15 == 0:
        continue
    if i % 5 == 0:
        print(i)