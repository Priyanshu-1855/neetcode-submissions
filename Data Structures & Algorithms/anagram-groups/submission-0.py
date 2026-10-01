class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        if n == 0 or n == 1:
            return [strs]

        ans = {}

        for i in range(n):
            key = "".join(sorted(strs[i]))
            if key not in ans:
                ans[key] = []
            ans[key].append(strs[i])


        res = []
        for val in ans.values():
            res.append(val)

        return res
            

