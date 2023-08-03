#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) return 0;
    
        int max_len = 0, curr_len = 0;
        vector<int> chars(256, -1);
        
        for (int i = 0; i < s.size(); i++) {
            if (chars[s[i]] == -1) {
                curr_len++;
            } else {
                max_len = max(max_len, curr_len);
                curr_len = min(curr_len + 1, i - chars[s[i]]);
            }
            
            chars[s[i]] = i;
        }
        
        return max(max_len, curr_len);
    }
};
