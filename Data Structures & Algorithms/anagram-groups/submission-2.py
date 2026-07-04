class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # second attempt
        values = {}
        for i in strs:
            sorted_i = str(sorted(i))
            temp = values.get(sorted_i, [])
            temp.append(i)
            values[sorted_i] = temp

        final_list = []
        for x in values.values():
            final_list.append(x)

        return final_list