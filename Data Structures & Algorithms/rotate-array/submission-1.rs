impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        // let n = nums.len();
        // let mut k = k as usize % n;
        // while k > 0 {
        //     let tmp = nums[n - 1];
        //     for i in (1..n).rev() {
        //         nums[i] = nums[i - 1];
        //     }
        //     nums[0] = tmp;
        //     k -= 1;
        // }
        // let n = nums.len();
        // let k = k as usize % n;
        // let mut tmp = vec![0;n];
        // for i in 0..n {
        //     tmp[(i + k)%n] = nums[i];
        // }
        // nums.copy_from_slice(&tmp);

        let n = nums.len();
        let k = k as usize % n;
        let mut count = 0;
        let mut start = 0;
        while count < n {
            let mut current = start;
            let mut prev = nums[start];
            loop {
                let next_idx = (current + k) % n;
                let temp = nums[next_idx];
                nums[next_idx] = prev;
                prev = temp;
                current = next_idx;
                count += 1;
                if start == current {
                    break;
                }
            }
            start += 1;
        }
    }
}
