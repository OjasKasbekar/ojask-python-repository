for i in range(2, 1001):
     for p in range(2, i):
        if (i % p) == 0:
            break
        else:
            print(i)
            break


