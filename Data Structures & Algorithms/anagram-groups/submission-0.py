class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dict1 = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            dict1[s].append(i)
        return list(dict1.values())
        