class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
            return False

        s = sorted(s)
        t = sorted(t)

        if s != t:
            return False

        return True