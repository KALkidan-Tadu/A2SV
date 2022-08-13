class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());
        int num = piles.size()/3;
        int sum=0;
        int i = piles.size()-2;
        while(i>=num){
            sum += piles[i];
            i -= 2; 
        }
        return sum;
    }
};
