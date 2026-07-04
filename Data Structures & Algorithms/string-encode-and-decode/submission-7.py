class Solution:

    def encode(self, strs: List[str]) -> str:
        # result += f"{length}#{s}"
        #slow O(n^2) as strings are immutable and are copied
        result = "".join(f"{len(s)}#{s}" for s in strs)
        #iterating through all the pieces once to calculate the total length, 
        #allocating memory once, then writing into it — so it's O(n).
        return result


    def decode(self, s: str) -> List[str]:
        decoded_s = []
        i: int = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])

            start = j + 1
            end = start + length

            decoded_s.append(s[start:end])

            i = end

        return decoded_s

