/**
 * Definition for singly-linked list.
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, int carry = 0) {
        if (!l1 && !l2) {
            return carry ? new ListNode(carry) : nullptr;
        }

        int sum;
        if (!l1) {
            sum = carry + l2->val;
            return new ListNode(sum % 10, addTwoNumbers(nullptr, l2->next, sum / 10));
        }
            
        if (!l2)
         {
            sum = carry + l1->val;
            return new ListNode(sum % 10, addTwoNumbers(l1->next, nullptr, sum / 10));
        }
        
        sum = carry + l1->val + l2->val;
        return new ListNode(sum % 10, addTwoNumbers(l1->next, l2->next, sum / 10));
    }
};
