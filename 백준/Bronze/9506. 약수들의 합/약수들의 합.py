while True:
    
    n = int(input())
    temp = []
    if n == -1:
        break
    
    for i in range(1,n):
        if n % i == 0: 
            temp.append(i)
    
    if sum(temp) == n: 
        print(n, "=", end = ' ')
        print(*temp, sep = ' + ')
    else:
        print("%d is NOT perfect." %n)       