class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        count = 1
        max_count = 1
        
        for i in range(len(nums) - 1):      # - 1 prevents IndexError
            if nums[i + 1] - nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            elif nums[i + 1] == nums[i]:
                continue                    # Skip duplicates
            else:
                count = 1                   # Reset streak
                
        return max_count                    # Indented outside the loop