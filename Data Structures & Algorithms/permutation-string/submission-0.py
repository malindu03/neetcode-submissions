class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        mp_target = {}
        mp = {}

        # initialise hash maps
        for r in range(len(s1)):
            mp[s2[r]] = mp.get(s2[r], 0) + 1
            mp_target[s1[r]] = mp_target.get(s1[r], 0) + 1

        if mp == mp_target:
            return True

        for i in range(len(s1), len(s2)):
            mp[s2[i]] = mp.get(s2[i], 0) + 1
            mp[s2[i - len(s1)]] -= 1

            if mp[s2[i - len(s1)]] == 0:
                del mp[s2[i - len(s1)]]

            if mp == mp_target:
                return True

        return False
