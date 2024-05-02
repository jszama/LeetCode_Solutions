class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            asArray = sorted(list(string))
            anagrams["".join(asArray)].append(string)

        return anagrams.values()
