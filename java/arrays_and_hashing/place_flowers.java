class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int placements = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0) {
                boolean left_open = (i == 0) || (flowerbed[i - 1] == 0);
                boolean right_open = (i == flowerbed.length - 1) || (flowerbed[i + 1] == 0);
                if (left_open && right_open) {
                    flowerbed[i] = 1;
                    if (++placements >= n) {
                        return true;
                    }
                }
            }
        }
        return placements >= n;
    }
}