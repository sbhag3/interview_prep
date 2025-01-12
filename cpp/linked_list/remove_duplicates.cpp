/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* trav = head;
        while (trav && trav->next) {
            if (trav->next->val == trav->val) {
                trav->next = trav->next->next;
                continue;
            }
            trav = trav->next;
        }
        return head;
    }
};