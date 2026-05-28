class Solution {
    public int[] getConcatenation(int[] nums) {
        int idx = 0;
        int [] ary = new int [2*nums.length];

        for (int i = 0; i < 2; i++) {
            for (int num : nums) {
                ary[idx++] = num;
            }
        }

        return ary;
        
    }
}