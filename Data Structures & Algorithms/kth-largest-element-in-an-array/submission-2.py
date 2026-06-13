class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = []

        while len(nums) != k:
            val = heapq.heappop(nums)
        
        return nums[0]