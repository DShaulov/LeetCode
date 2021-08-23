#Edge cases
# 1."aaa123"
#  escape letter sequence and upper/lower/digit with one change 


class Solution:
    @staticmethod
    def strongPasswordChecker(password: str) -> int:
        #Check password length
        passLenSteps = 0
        if len(password) < 6:
            passLenSteps = 6 - len(password)
        elif len(password) > 20:
            passLenSteps = len(password) - 20
            
        #Check lower/upper
        upperLowerDigitSteps = 0
        upperLowerDigit = [0, 0, 0]
        for letter in password:
            if ord(letter) >= 65 and ord(letter) <= 90:
                upperLowerDigit[0] = 1
            elif ord(letter) >= 97 and ord(letter) <= 122:
                upperLowerDigit[1] = 1
            elif ord(letter) >= 48 and ord(letter) <= 57:
                upperLowerDigit[2] = 1
        for i in range(3):
            if upperLowerDigit[i] == 0:
                upperLowerDigitSteps += 1

        if len(password) < 6:
            actualSteps =  upperLowerDigitSteps - (6 - len(password))
            if actualSteps > 0 :
                passLenSteps += actualSteps
        else:
            passLenSteps += upperLowerDigitSteps
        
        #Check repeating characters
        repeatingSeqSteps = 0
        i = 0
        while i < (len(password)):
            numOfRepeatingChars = 0
            j = i
            while j < (len(password) - i):
                if password[i] == password[j]:
                    numOfRepeatingChars += 1
                    j += 1
                else:
                    if numOfRepeatingChars >= 3:
                        repeatingSeqSteps += numOfRepeatingChars - 2
                    break
            i = j
        for number in upperLowerDigit:
            if number == 0 and repeatingSeqSteps > 0:
                repeatingSeqSteps - 1
        
        passLenSteps += repeatingSeqSteps
        return passLenSteps
 
                    
                
if __name__ == "__main__":
    print(Solution.strongPasswordChecker("a"))
    print(Solution.strongPasswordChecker("aA1"))
    print(Solution.strongPasswordChecker("1337C0d3"))
    print(Solution.strongPasswordChecker("1"))
    print(Solution.strongPasswordChecker("aA123"))
    print(Solution.strongPasswordChecker("aaa111"))
    print(Solution.strongPasswordChecker("aaa123"))





