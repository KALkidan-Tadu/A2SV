class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
       long long i=0, j=1, answer=1;
        while(j<prices.size()){
            if(prices[j-1]-prices[j] == 1){
                answer+=j-i+1;
            }else{
                i = j;
                answer+=j-i+1;
            }
            j++;                
        }
        return answer;
    }
};
