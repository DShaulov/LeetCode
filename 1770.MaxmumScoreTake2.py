from __future__ import annotations

# Solved a harder problem by accident, didnt read instructions correctly


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        score = 0
        while(multipliers != []):
            startNum = nums[0]
            endNum = nums[-1]
            # Find the smallest and largest multi
            largestMulti = 0
            smallestMulti = 0
            for multi in multipliers:
                if multi > largestMulti:
                    largestMulti = multi
                if multi < smallestMulti:
                    smallestMulti = multi
            bestOption = -100001
            bestOptionsIndex = 0
            allOptions = [
                startNum * largestMulti,
                startNum * smallestMulti,
                endNum * largestMulti,
                endNum * smallestMulti
            ]
            for i in range(len(allOptions)):
                if allOptions[i] > bestOption:
                    bestOption = allOptions[i]
                    bestOptionsIndex = i
            
            score += bestOption
            print("Best option:", bestOption)
            if bestOptionsIndex == 0:
                nums.remove(startNum)
                multipliers.remove(largestMulti)
            elif bestOptionsIndex == 1:
                nums.remove(startNum)
                multipliers.remove(smallestMulti)
            elif bestOptionsIndex == 2:
                nums.remove(endNum)
                multipliers.remove(largestMulti)
            else:
                nums.remove(endNum)
                multipliers.remove(smallestMulti)

        return score
                       

if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.maximumScore([1,2,3], [3,2,1]))
    print("Expected: 14")
    print(mySolution.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
    print("Expected: 102")