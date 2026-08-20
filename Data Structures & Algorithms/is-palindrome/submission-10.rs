impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut left = 0;
        
        let s_chars: Vec<char> = s.to_uppercase().chars().collect();
        let mut right = s_chars.len() - 1;
        while left < right {
            if !s_chars[left].is_alphanumeric() {
                left += 1;
                continue;
            }
            if !s_chars[right].is_alphanumeric() {
                right -= 1;
                continue;
            }
            if s_chars[left] != s_chars[right] {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;

    }
}
