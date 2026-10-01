class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_cnt = {}
        for i in range(len(nums)):
            freq_cnt[nums[i]] = freq_cnt.get(nums[i],0)+1

        ans = []
        for _ in range(k):
            max_num = max(freq_cnt,key = freq_cnt.get)
            ans.append(max_num)
            freq_cnt[max_num] = -1

        return ans

                


