from typing import List
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        solution = []
        while len(strs) != 0:
            word = strs[0]
            group = [word]
            for i in range(1, len(strs)):
                if len(word) != len(strs[i]):
                    continue
                anagram = True
                for j in range(len(word)):
                    if word[j] not in strs[i]:
                        anagram = False
                        break
                    elif word.count(word[j]) != strs[i].count(word[j]):
                        anagram = False
                        break
                if anagram:
                    group.append(strs[i])
            for string in group:
                strs.remove(string)
            solution.append(group)
        return solution



if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(solution.groupAnagrams([""]))
    print(solution.groupAnagrams(["a"]))
    print(solution.groupAnagrams(["ddddddddddg","dgggggggggg"]))

