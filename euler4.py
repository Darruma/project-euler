maxVal = 0
for i in range(100,1001):
    for j in range(100,1001):
        val = int(str(i*j)[::-1])
        if (val  == i * j):
            if val > maxVal:
                maxVal = val;

print(maxVal)
