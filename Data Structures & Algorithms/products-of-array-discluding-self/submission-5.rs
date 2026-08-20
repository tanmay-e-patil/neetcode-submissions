impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        
        let n = nums.len();
        let mut res = vec!(1i32;n);
        let mut lpp = vec!(1i32;n);
        let mut rpp = vec!(1i32;n);

        for i in 1..n {
            lpp[i] = lpp[i - 1] * nums[i - 1]; 
        }

        for i in (0..n-1).rev() {
            rpp[i] = rpp[i + 1] * nums[i + 1];
        }

        for i in 0..n {
            res[i] = lpp[i] * rpp[i];
        }
        res
        // for i in 0..n {
        //     for j in 0..n {
        //         if i == j {
        //             continue
        //         }
        //         res[i] *= nums[j];
        //     }
        // }
        // res

    }
}
