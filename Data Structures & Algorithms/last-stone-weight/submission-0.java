class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> weights = new PriorityQueue<>();
        for (int s: stones) {
            weights.offer(-s);
        }

        while (weights.size() > 1) {
            int first = weights.poll();
            int second = weights.poll();
            if (first < second) {
                weights.offer(first - second);
            }
        }

        weights.offer(0);
        return Math.abs(weights.peek());
        
    }
}
