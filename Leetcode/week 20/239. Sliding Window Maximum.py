class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')

        for i, v in enumerate(nums):
            window.append(v)
            if i < k-1:
                continue

            # 아직 최대값이 반영된 상태가 아닐 때
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max: # 이미 최대값이 존재할 경우, 새로 추가된 값이 기존 최대값보다 더 큰경우에만 최대값 교체
                current_max = v

            results.append(current_max)

            # max값이 빠져나갈 경우
            if current_max == window.popleft():
                current_max = float('-inf')
        return results