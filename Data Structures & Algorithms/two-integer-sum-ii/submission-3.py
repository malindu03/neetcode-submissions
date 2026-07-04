class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Time complexity: nlogn , space: 1 - binary search

        for i in range (len(numbers)):
            temp = target - numbers[i]
            left, right = i + 1, len(numbers) - 1

            while left <= right:
                mid = left + (right - left)//2
                if numbers[mid] == temp:
                    return [i+1, mid + 1]
                elif numbers[mid] < temp:
                    left = mid + 1
                else:
                    right = mid - 1

        return []