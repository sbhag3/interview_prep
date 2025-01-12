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
    ListNode* reverseList(ListNode* head) {
        stack<ListNode*> st;
        ListNode* tmp = head;
        while (tmp) {
            st.push(tmp);
            tmp = tmp->next;
        }
        ListNode* trav = new ListNode();
        ListNode* before_head = trav;
        while (!st.empty()) {
            trav->next = new ListNode(st.top()->val);
            st.pop();
            trav = trav->next;
        }
        return before_head->next;
    }
};