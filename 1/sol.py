class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in seen:
                return [seen[needed],i]
            else:
                seen[nums[i]] = i
