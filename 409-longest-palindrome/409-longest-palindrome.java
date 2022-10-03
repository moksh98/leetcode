class Solution {
    public int longestPalindrome(String s) {
        Map<String, Integer> frequency = new HashMap<>();
        int length = 0;
        for(int i = 0; i < s.length(); i++) {
            frequency.put(s.substring(i, i+1), frequency.getOrDefault(s.substring(i, i+1), 0) + 1);
            if(frequency.get(s.substring(i, i+1)) % 2 == 0) {
                length += 2;
                frequency.remove(s.substring(i, i+1));
            }
        }
        return frequency.size() > 0 ? length+1 : length;
    }
}