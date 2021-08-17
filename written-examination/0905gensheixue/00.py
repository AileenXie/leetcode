# def func(n):
#     dp=[0]*(n+1)
#     dp[0]=1
#     dp[1]=1
#     for i in range(1,n+1):
#         dp[i]=dp[i-1]+dp[i-2]
#     return dp[-1]

import random
def birth_trials_needed_to_get_boy_and_girl():
    girl,boy=0,0
    for i in range(100000):
        total=0
        while not girl or not boy:
            cur = random.randint(0,1)
            if cur:
                boy+=1
            else:
                girl+=1
            total+=1
        print(total)
