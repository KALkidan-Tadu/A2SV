class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i=0, j=0, maxlen=0, len=0;
        unordered_map<char,int> mymap;
        while(j<s.length()){
            if(mymap[s[j]]>0){
                len = j-i;
                maxlen = max(maxlen, len);
                while(s[j]!=s[i]){
                    mymap[s[i]]--;
                    i++;
                }mymap[s[i]]--;
                 i++;
            }else if(j==s.length()-1){
                len = j-i+1;
                maxlen = max(maxlen, len);
            }
            mymap[s[j]]++;
            j++;
        }
        return maxlen;
    }
};
