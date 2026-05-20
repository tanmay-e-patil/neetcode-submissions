class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] leftProduct = new int[nums.length];

        int product = 1;
        for (int i = 0; i < nums.length; i++) {
            leftProduct[i] = product;
            product *= nums[i];
        }

        product = 1;
        int [] rightProduct = new int[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            // 1,1,2,8
            // 48,24,6,1
            rightProduct[i] = product;
            product *= nums[i];
        }

        int [] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = leftProduct[i] * rightProduct[i];
        }

        return result;


        
    }
}  
