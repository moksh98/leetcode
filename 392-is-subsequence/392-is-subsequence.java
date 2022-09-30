class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length() == 0) {
            return true;
        }
        int pointer_s = -1;
        int pointer_t = -1;
        for(int i = 0; i < t.length(); i++) {
            if(s.charAt(pointer_s+1) == t.charAt(pointer_t+1)) {
                pointer_s += 1;
            }
            if(s.length()-1 == pointer_s) {
                return true;
            }
            pointer_t += 1;
        }
        return false;
    }
}