impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut mp = 0;
        let n = prices.len();

        for i in 0..n {
            for j in i..n {
                mp = mp.max(prices[j] - prices[i]);
            }
            println!("{:?}", mp);
        }
        return mp;
    }
}
