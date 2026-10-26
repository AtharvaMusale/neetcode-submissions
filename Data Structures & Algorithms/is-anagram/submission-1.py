class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        for n in s:
            hashs[n] = hashs.get(n,0)+1

        hasht = {}
        for n in t:
            hasht[n] = hasht.get(n,0)+1

        return hashs == hasht
