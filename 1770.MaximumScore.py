from __future__ import annotations

# Solved a harder problem by accident, didnt read instructions correctly


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        score = 0
        positiveNums = [x for x in nums if x > 0]
        positiveMults = [x for x in multipliers if x > 0]
        negativeNums = [abs(x) for x in nums if x < 0]
        negativeMults = [abs(x) for x in multipliers if x < 0]
        

        while (positiveNums != [] and positiveMults != [] and negativeNums !=[] and negativeMults != []):
            # Find the largest 
            largestPosNum = 0
            largestPosMult = 0
            largestNegNum = 0
            largestNegMult = 0

            for number in positiveNums:
                if number > largestPosNum:
                    largestPosNum = number
            for number in negativeNums:
                if number > largestNegNum:
                    largestNegNum = number
            
            for mult in positiveMults:
                if mult > largestPosMult:
                    largestPosMult = mult
            for mult in negativeMults:
                if mult > largestNegMult:
                    largestNegMult = mult

            if (largestNegMult * largestNegNum < largestPosNum * largestPosMult):
                score += largestPosNum * largestPosMult
                positiveNums.remove(largestPosNum)
                positiveMults.remove(largestPosMult)
            else:
                score += largestNegNum * largestNegMult
                negativeNums.remove(largestNegNum)
                negativeMults.remove(largestNegMult)
        if (negativeNums == [] or negativeMults == []):
            while (positiveMults != [] and positiveNums != []):
                largestNum = 0
                largestMult = 0

                for number in positiveNums:
                    if number > largestNum:
                        largestNum = number
                for mult in positiveMults:
                    if mult > largestMult:
                        largestMult = mult

                score += largestMult * largestNum
                positiveMults.remove(largestMult)
                positiveNums.remove(largestNum)
        else:
            while (negativeMults != [] and negativeNums != 0):
                largestNum = 0
                largestMult = 0

                for number in negativeNums:
                    if number > largestNum:
                        largestNum = number
                for mult in negativeMults:
                    if mult > largestMult:
                        largestMult = mult

                score += largestMult * largestNum
                negativeMults.remove(largestMult)
                negativeNums.remove(largestNum)
        return score
                       

if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.maximumScore([1,2,3], [3,2,1]))
    print("Expected: 14")
    print(mySolution.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
    print("Expected: 102")

