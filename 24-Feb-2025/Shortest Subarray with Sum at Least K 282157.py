# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)  # Prefix sum array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        min_len = float('inf')
        dq = deque()  # Monotonic deque to store indices

        for right in range(n + 1):
            while dq and prefix_sum[right] - prefix_sum[dq[0]] >= k:
                min_len = min(min_len, right - dq.popleft())

            while dq and prefix_sum[right] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(right)

        return min_len if min_len != float('inf') else -1
