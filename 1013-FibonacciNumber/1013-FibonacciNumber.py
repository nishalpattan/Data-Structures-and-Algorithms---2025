# Last updated: 8/3/2025, 9:02:37 PM
class Solution:
    def fib(self, N: int, memo = dict()) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        elif N in memo:
            return memo[N]
        else:
            memo[N] = self.fib(N-1) + self.fib(N-2)
        return memo[N]
        # TC : O(2^N) approach
        # if N == 0 :
        #     return 0
        # elif N == 1:
        #     return 1
        # else:
        #     return self.fib(N-1)+self.fib(N-2)