use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new();
        let n = nums.len();
        for num in nums {
            set.insert(num);
        }
        set.len() < n
    }
}
