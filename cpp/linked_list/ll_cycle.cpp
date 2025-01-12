/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *start = head;
        ListNode *end = head;
        while (end && end->next) {
            start = start -> next;
            end = end->next->next;
            if (start == end) {
                return true;
            }
        }
        return false;

        // ListNode* slow = head;
        // ListNode* fast = head;
        // while (fast && fast->next) {
        //     slow = slow->next;
        //     fast = fast->next->next;
        //     if (slow == fast) return true;
        // }
        // return false;
        
    }
};