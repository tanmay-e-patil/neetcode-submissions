class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> complement = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int complementNum = target - num;
            if (complement.containsKey(num)) {
                return new int[] {complement.get(num), i};
            }
            complement.put(complementNum, i);
        }
        return new int[]{-1, -1};
    }
}
