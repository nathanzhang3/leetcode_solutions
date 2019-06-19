class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDist = self.getAlphabetDist(p)
        pos = []
        windowDist = self.getAlphabetDist(s[:len(p)])
        if pDist == windowDist:
            pos.append(0)
        for i in range(len(s)-len(p)):
            losingChar = s[i]
            gainingChar = s[i + len(p)]
            windowDist[ord(losingChar)-ord('a')] -= 1
            windowDist[ord(gainingChar)-ord('a')] += 1
            if windowDist == pDist:
                pos.append(i+1)
        return pos
        
    def getAlphabetDist(self, p):
        dist = [0]*26
        for char in p:
            dist[ord(char)-ord('a')] += 1
        return dist
