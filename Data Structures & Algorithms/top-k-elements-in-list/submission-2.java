class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count how many times a number appears
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Create a MIN Heap ordered by frequency
        // The element with the SMALLEST frequency will always be at the top
        PriorityQueue<Integer> minHeap = 
            new PriorityQueue<>((a,b) -> freq.get(a) - freq.get(b));

        // Add every unique number into the heap
        // If the heap grows larger than k, remove it from the heap
        for (int num : freq.keySet()) {
            minHeap.offer(num);

            if (minHeap.size() > k) {
                minHeap.poll();
            }

        }

        // Since the heap has the k most frequent numbers, extract into the result array
        int[] result = new int[k];
        
        //Fill backwards because the heap returns lowest frequency to highest frequency
        for (int i = k - 1; i >= 0; i--) {
            result[i] = minHeap.poll();
        }

        return result;




    }
}
