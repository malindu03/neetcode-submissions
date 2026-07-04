class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        total = len(A) + len(B)


        if len(B) < len(A):
            A, B = B, A

        lo, hi = 0, len(A)
        half = (total  + 1) // 2

        while lo <= hi:
            i = lo + (hi - lo) // 2
            j = half - i

            left1 = A[i-1] if i > 0 else float('-inf')
            right1 = A[i] if i < len(A) else float('inf')
            left2 = B[j-1] if j > 0 else float('-inf')
            right2 = B[j] if j < len(B) else float('inf')

            if left1 > right2:
                hi = i - 1
            elif left2 > right1:
                lo = i + 1
            else:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
