class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mp = new HashMap<Integer, Integer>();


        for (int i = 0; i < nums.length; i++) {
            if (mp.containsKey(nums[i])) {
                return new int[]{mp.get(nums[i]), i};
            }

            int complement = target - nums[i];
            mp.put(complement, i);

        }
        return new int[]{-1,-1};
    }
}
