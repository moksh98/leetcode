class Solution {
    public int coinChange(int[] coins, int amount) {
        int dp[] = new int[amount+1];
        Arrays.fill(dp, amount+1);
        dp[0] = 0;
        Arrays.sort(coins);
        for(int i = 0; i < amount+1; i++) {
            for(int j : coins) {
                if(j <= i) {
                    dp[i] = Math.min(dp[i], dp[i-j]+1);
                }
                else {
                    break;
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}