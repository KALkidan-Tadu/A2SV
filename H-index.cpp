class Solution {
public:
    int hIndex(vector<int>& citations) {
         if (citations.size()==1 and citations[0]==0)
            return 0;
        sort(citations.begin(), citations.end(), greater<int>());
        int i=0;
        int c=1;
        while (i<citations.size() && c<= citations[i]){
            i+=1;
            c+=1;
        }
        return c-1;
    }
};
