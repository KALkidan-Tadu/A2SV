class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> answer;
        unordered_map<char, int>pmap;
        unordered_map<char, int>smap;
        for(int i=0; i<p.length(); i++)
            pmap[p[i]]++;
        int left=0, right=0;
        while(right<s.length()){
            if(pmap.find(s[right])!=pmap.end() && smap[s[right]]<pmap[s[right]]){
                smap[s[right]]++;
                if(right-left+1 == p.length()){
                    answer.push_back(left);
                    smap[s[left]]--;
                    left++;
                }
            }
            else if(pmap.find(s[right])==pmap.end()){
                while(left<=right){
                    smap[s[left]]--;
                    left++;
                }
            }else{
                smap[s[left]]--;
                left++;
                right--;
            }
            right++;
        }
       return answer; 
    }
};
