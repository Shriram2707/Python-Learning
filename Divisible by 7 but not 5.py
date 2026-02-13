#Assignment - Loops - Divisible by 7 but not 5
l = []
for i in range(2000, 3001):
    if (i % 7 == 0) or (i % 5 != 0):
        l.append(str(i))
        print(','.join(l))

        
