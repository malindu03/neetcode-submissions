from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # second attempt
        values = defaultdict(list)
        for i in strs:
            sorted_i = str(sorted(i))
            temp = values.get(sorted_i, [])
            temp.append(i)
            values[sorted_i] = temp

        return list(values.values())