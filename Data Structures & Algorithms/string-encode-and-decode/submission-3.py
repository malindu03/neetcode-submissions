class Solution:
    #naive
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "[EMPTY]"
        result = "_|_".join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        if s == "[EMPTY]":
            return []

        result = s.split("_|_")
        return result
