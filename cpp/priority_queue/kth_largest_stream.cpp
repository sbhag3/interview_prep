class KthLargest {
public:
    int k_;
    priority_queue<int, vector<int>, greater<int>> pq;
    KthLargest(int k, vector<int>& nums) {
        k_ = k;
        for (int i : nums) {
            pq.push(i);
        }
        while (pq.size() > k) {
            pq.pop();
        }
    }
    
    int add(int val) {
        pq.push(val);
        if (pq.size() > k_) pq.pop();
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */