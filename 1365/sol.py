class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        count = defaultdict(int)
        res = []
        for i in range(len(temp)):
            if temp[i] not in count.keys():
                count[temp[i]] = i
        for i in range(len(nums)):
            res.append(count[nums[i]])

        return res
