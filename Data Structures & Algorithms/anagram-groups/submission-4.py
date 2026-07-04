from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # second attempt
        values = defaultdict(list)
        for i in strs:
            sorted_i = str(sorted(i))
            values[sorted_i].append(i)

        return list(values.values())