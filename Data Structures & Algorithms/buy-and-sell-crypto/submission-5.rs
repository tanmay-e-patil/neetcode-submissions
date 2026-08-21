impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut mp = 0;
        let n = prices.len();

        let mut l = 0;
        let mut r = 0;
        while r < n {
            if prices[l] < prices[r] {
                let profit = prices[r] - prices[l];
                mp = mp.max(profit);
            } else {
                l = r;
            }
            r += 1;
        }
        mp
    }
}
