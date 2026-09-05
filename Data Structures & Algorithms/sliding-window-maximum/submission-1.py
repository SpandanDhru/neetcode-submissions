class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0
        q = collections.deque() # indexes stored

        for r in range(len(nums)):
            # remove indicies whoese values are smaller than nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove indcies outside the window
            if q[0] < l:
                q.popleft()
            
            # window has reached size k
            if r - l + 1 == k:
                output.append(nums[q[0]])
                l += 1
        return output




        