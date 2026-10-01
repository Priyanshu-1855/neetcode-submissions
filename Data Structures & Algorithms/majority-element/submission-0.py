class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        freq = {}
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        maj_ele = max(freq, key = freq.get)
        return maj_ele
            