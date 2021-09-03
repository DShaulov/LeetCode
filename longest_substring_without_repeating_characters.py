class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestSubstring = 0
        if len(s) > 0:
            longestSubstring = 1
        for i in range(len(s)):
            substringChars = []
            substringChars.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in substringChars:
                    substringChars.append(s[j])
                    if longestSubstring < len(substringChars):
                        longestSubstring = len(substringChars)
                    if j == len(s) - 1:
                        return longestSubstring
                else:
                    break
        return longestSubstring
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("xxzqi"))


