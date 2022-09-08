class Solution {
    public int subarraySum(int[] nums, int k) {
        int current_sum = 0;
        int count = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, 1);
        for(int num : nums) {
            current_sum += num;
            if(map.containsKey(current_sum-k)) {
                count += map.get(current_sum-k);
            }
            map.put(current_sum, map.getOrDefault(current_sum, 0) + 1);
        }
        return count;
    }
}