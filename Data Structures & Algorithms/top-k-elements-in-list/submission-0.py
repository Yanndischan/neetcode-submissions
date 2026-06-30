class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        pairs = []
        count = 1
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                pairs.append((count, nums[i]))
                count = 1
            else:
                count += 1

        pairs.sort(key=lambda x: x[0], reverse=True)
        result = []
        for i in range(k):
            result.append(pairs[i][1])
            
        return result