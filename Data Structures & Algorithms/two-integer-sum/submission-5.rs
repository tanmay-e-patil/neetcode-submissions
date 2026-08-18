impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for (i, &n) in nums.iter().enumerate() {
            let diff = target - n;
            if let Some(&index) = map.get(&diff) {
                return vec![index as i32, i as i32];
            }
            map.insert(n, i);
        }

        vec![]

    }
}
