class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        for char in t:
            count [char] -= 1

        temp = set(count.values())

        if len(temp) == 1 and temp.pop() == 0:
            return True
        return False
