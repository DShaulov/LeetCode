class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = -x
        totalNum = 0
        numPower = len(str(x)) - 1
        while x >= 1:
            lastDigit = x % 10
            if totalNum + pow(lastDigit, numPower) >= pow(2, 31) - 1:
                return 0
            elif totalNum + pow(lastDigit, numPower) <= - pow(2, 31):
                return 0
            else:
                totalNum = totalNum + (lastDigit * pow(10, numPower))
                numPower = numPower - 1
                x = x // 10
        if negative:
            totalNum = - totalNum
        return totalNum

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(-123))