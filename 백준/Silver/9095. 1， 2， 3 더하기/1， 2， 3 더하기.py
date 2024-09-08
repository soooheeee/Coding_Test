import sys
input = sys.stdin.readline

n = int(input())  

for i in range(1, n+1):
    n_2 = int(input())
    
    dp = [0] * (n_2 + 3)  
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for j in range(4,n_2+1):
      dp[j] = dp[j-3] + dp[j-2] + dp[j-1]
 
    print(dp[n_2])

