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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;
        return mergeHelper(lists, 0, lists.size() - 1);
    }
    ListNode* mergeHelper(vector<ListNode*>& lists, int start, int end) {
        if (start > end) return nullptr;
        if (start == end) return lists[start];

        int mid = (start + end) / 2;
        ListNode* left = mergeHelper(lists, start, mid);
        ListNode* right = mergeHelper(lists, mid + 1, end);
        return merger(left, right);
    }
    ListNode* merger(ListNode* node1, ListNode* node2) {
        ListNode* head = new ListNode(-1);
        ListNode* trav = head;

        while (node1 && node2) {
            if (node1->val < node2->val) {
                trav->next = node1;
                node1 = node1->next;
            } else {
                trav->next = node2;
                node2 = node2->next;
            }
            trav = trav->next;
        }
        trav->next = (node1) ? node1 : node2;
        return head->next;
    }
};