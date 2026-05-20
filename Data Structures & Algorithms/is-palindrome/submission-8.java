class Solution {
    public boolean isPalindrome(String s) {
        char [] letters = s.toCharArray();
        int left = 0;
        int right = letters.length - 1;
        
        while (left < right) {
            if (!Character.isLetterOrDigit(letters[left])) {
                left++;
                continue;
            }
            else if (!Character.isLetterOrDigit(letters[right])) {
                right--;
                continue;
            }
            else {
                if (!(Character.toLowerCase(letters[left]) == Character.toLowerCase(letters[right]))) {
                    return false;
                }
                left++;
                right--;
            }


        }
        return true;
        
    }
}
