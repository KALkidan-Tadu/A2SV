class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i=0, max = 0, count = 1;
        while(i<s.length()){
            int count = 0;
            unordered_map<char,int> myMap;
            for(int j=i; j<s.length(); j++){
                if(myMap[s[j]] > 0){
                    if(count> max)
                        max = count;
                    break;
                }
                else{
                    myMap[s[j]]++;
                    count++;
                }
            }
           if(count> max)
                max = count; 
            i++;
        }
        return max;
    }
};
