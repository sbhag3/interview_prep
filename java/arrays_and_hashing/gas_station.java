class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int curr = 0, total = 0, ans = 0;

        for (int i = 0; i < gas.length; i++) {
            total += gas[i] - cost[i];
            curr += gas[i] - cost[i];

            if (curr < 0) {
                ans = i + 1;
                curr = 0;
            }
        }

        return (total >= 0) ? ans : -1;
    }
}