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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* final_list = new ListNode();
        ListNode* curr_ptr{final_list};

        int sum, carry{0};
        while (l1 || l2) {
            sum = carry;
            if (l1) sum += l1->val;
            if (l2) sum += l2->val;
            carry = sum / 10;

            ListNode* new_node = new ListNode(sum % 10);
            curr_ptr->next = new_node;
            curr_ptr = new_node;

            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        if (carry) {
            ListNode* new_node = new ListNode(carry);
            curr_ptr->next = new_node;
            curr_ptr = new_node;
        }

        return final_list->next;
    }
};
