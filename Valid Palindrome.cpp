class Solution {
public:
    bool isPalindrome(string s) {
        string word = "";
        for(int i=0; i<s.length(); i++){
            if(isalpha(s[i]) || isdigit(s[i]))
                word.push_back(tolower(s[i]));
        }
        int left=0, right=word.length()-1;
        while(left<=right){
            if(word[left] != word[right])
                return false;
            else{
                left++;
                right--;
            }
        }
        return true;
    }
};
