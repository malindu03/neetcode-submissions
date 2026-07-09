class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == s2_count[i])

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            i = ord(s2[r]) - ord('a')
            s2_count[i] += 1
            
            if s2_count[i] == s1_count[i]:
                matches += 1
            elif s1_count[i] + 1 == s2_count[i]:
                matches -= 1


            i = ord(s2[l]) - ord('a')
            s2_count[i] -= 1

            if s1_count[i] == s2_count[i]:
                matches += 1
            elif s1_count[i] - 1 == s2_count[i]:
                matches -= 1

            l += 1

        return matches == 26
            