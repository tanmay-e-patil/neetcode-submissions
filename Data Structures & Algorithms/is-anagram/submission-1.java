class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] s2= new int[26];
        int[] t2 = new int[26];
        for(int i = 0; i< 26; i++) {
            s2[i] = 0;
            t2[i] = 0;
        }
        for(int i = 0; i < s.length(); i++) {
            int sidx = ((int) s.charAt(i)) - (int)'a';
            s2[sidx]++;
            int tidx = ((int) t.charAt(i)) - (int)'a';
            t2[tidx]++;
        }
        
        for (int i = 0; i< 26; i++) {
            // System.out.println(s2[i], t2[i])
            if (s2[i] != t2[i]) {
                return false;
            }
        }
        return true;

    }
}
