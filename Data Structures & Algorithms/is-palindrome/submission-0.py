class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        t = "".join(ch for ch in s if ch.isalnum())

        i , j = 0, len(t)-1
        while i <= j:
            if t[i] != t[j]:
                return False

            i += 1
            j -= 1


        return True