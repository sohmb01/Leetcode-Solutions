# Problem ID: 68
# Title: Text Justification
# Runtime: 0 ms

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        while i < len(words):
            temp = []
            currWidth = 0
            wordsWidth = 0
            while currWidth < maxWidth and i < len(words):
                word = words[i]
                currWidth += len(word)
                if currWidth > maxWidth:
                    currWidth -= len(word)
                    break
                wordsWidth += len(word)
                currWidth+= 1
                temp.append(word)
                temp.append(" ")
                i+=1
            
            totalSpaces = maxWidth - wordsWidth
            spaces = (len(temp) // 2) - 1
            if spaces:
                s, r = totalSpaces // spaces , totalSpaces%spaces
            else:
                s, r = totalSpaces, 0
            idx = 1
            while idx < len(temp):
                k = (" " * s)
                if r:
                    r-=1
                    k+= " "
                temp[idx] = k
                idx+=2
            print(temp)
            ele = temp.pop()

            if ele and ele[0] != " ":
                temp.append(ele)
            line = "".join(temp)
            diff = maxWidth - len(line)
            line+= " " * diff
            ans.append(line)
        last = ""
        for i in range(len(temp)):
            if i%2 ==0:
                last+= temp[i] + " "
        diff = maxWidth - len(last)
        if diff<0:
            last = last[:maxWidth]
        else:
            last += " "*diff
        ans[-1] = last
        return ans


            
        