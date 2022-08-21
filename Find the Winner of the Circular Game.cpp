class Solution {
public:
    int findTheWinner(int n, int k) {
        vector<int> players;
        for(int i=1; i<=n; i++){
            players.push_back(i);
        }
        int start=0, count=1;
        while(players.size()>1){
            if(count==k){
                players.erase(players.begin()+start);
                count = 0;
                start--;
            }
            start++;
            if(start>=players.size())
                start=0;
            count++;
        }
        return players[0]; 
    }
};
