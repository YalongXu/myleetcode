class Solution:
    def divisorGame(self, N: int) -> bool:
        isFirst = True
        while True:
            isFirst = not isFirst
            divisor = isDivide(N)
            if divisor != 0:
                N -= divisor
            else:
                break
        return isFirst
        pass

def isDivide(N: int) -> int:
    for divisor in range(1, N//2+1):
        if N % divisor == 0:
            return divisor
    return 0

N = 2
mySolution = Solution()
print(mySolution.divisorGame(N))

N = 3
print(mySolution.divisorGame(N))


