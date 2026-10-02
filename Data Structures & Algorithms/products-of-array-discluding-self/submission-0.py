class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(0,len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             prod *= nums[j]

        #     res.append(prod)

        # return res


        n = len(nums)

        ans = [1]*n

        # Prefix
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # Suffix
        suffix = 1
        for i in range(n-1,-1,-1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans














