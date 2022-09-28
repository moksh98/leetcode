public class runningSumOf1DArray_1480 {
    public static int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];
        ans[0] = nums[0];
        for(int i = 1; i < nums.length; i++) {
            ans[i] = ans[i-1]+nums[i];
        }
        return ans;
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        System.out.println(runningSum(arr));
    }
}
