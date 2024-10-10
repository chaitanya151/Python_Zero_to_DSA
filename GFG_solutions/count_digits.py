class Solution:
    def evenlyDivides(self, N):
        count = 0
        num = N
        while N > 0:
            ld = N % 10
            N = N // 10
            if ld != 0 and num % ld == 0:
                count += 1
        return count
