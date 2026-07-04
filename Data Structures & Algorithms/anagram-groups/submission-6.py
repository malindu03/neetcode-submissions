class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first attempt O(n² × m)
        group = []
        added = set()
        for i in range(len(strs)):
            if i not in added:
                added.add(i)
                curr=[strs[i]]

                for j in range(i+1, len(strs)):
                    if j not in added:
                        if len(strs[i]) != len(strs[j]): continue

                        map_i, map_j = {}, {}
                        for x in range(len(strs[i])):
                            map_i[strs[i][x]] = map_i.get(strs[i][x],0) + 1
                            map_j[strs[j][x]] = map_j.get(strs[j][x],0) + 1

                        if map_i == map_j: 
                            curr.append(strs[j])
                            added.add(j)
                group.append(curr)

        return group
            