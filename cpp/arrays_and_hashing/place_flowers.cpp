class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int placements = 0;
        for (int i = 0; i < flowerbed.size(); i++) {
            if (flowerbed[i] == 0) {
                bool left_open = (i == 0) || (flowerbed[i - 1] == 0);
                bool right_open = (i == flowerbed.size() - 1) || (flowerbed[i + 1] == 0);
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
};