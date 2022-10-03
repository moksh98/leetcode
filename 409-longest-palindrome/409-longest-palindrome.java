class Solution {
    public int longestPalindrome(String s) {
        Map<String, Integer> frequency = new HashMap<>();
        int length = 0;
        for(int i = 0; i < s.length(); i++) {
            String ch = s.substring(i, i+1);
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
            if(frequency.get(ch) % 2 == 0) {
                length += 2;
                frequency.remove(ch);
            }
        }
        return frequency.size() > 0 ? length+1 : length;
    }
}