class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[0]*26
        for i in s:
            l[ord(i)-97]+=1
        for j in t:
            l[ord(j)-97]-=1
        for k in l:
            if k!=0:
                return False
        return True

        