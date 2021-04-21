class Solution:
    # Solution 1 228ms
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                # mid를 left와 right의 중앙으로 설정
                # 버퍼오버플로우를 발생시키지 않으려면 left + (right - left) // 2 를 사
                mid = (left + right) // 2

                # mid가 target보다 작을 경우, mid를 오른쪽으로 이동
                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                # mid가 target보다 큰 경우, mid를 왼쪽으로 이동
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                # mid와 target이 일치하는 경우
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)

    # Solution 2 240ms
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) //2

            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1

    # Solution 4 232ms
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1