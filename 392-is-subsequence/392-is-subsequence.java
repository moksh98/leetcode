class Solution {
    public boolean isSubsequence(String s, String t) {

        int pointer_s = 0;
        int pointer_t = 0;
        while(pointer_s < s.length() && pointer_t < t.length()) {
            if(s.charAt(pointer_s) == t.charAt(pointer_t)) {
                pointer_s += 1;
            }
            pointer_t += 1;
        }
        return pointer_s == s.length();
    }
}