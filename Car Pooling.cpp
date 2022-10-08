class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> dropoff;
        sort(trips.begin(), trips.end(), compare);
        int currentcap = 0;
        for(auto i: trips){
            currentcap += i[0];
            while(!dropoff.empty() && dropoff.top().first<=i[1]){
                currentcap -= dropoff.top().second;
                dropoff.pop();
            }
            if(currentcap>capacity)
                return false;
            dropoff.push({i[2], i[0]});
        }
        return true;
    }
    bool static compare(vector<int>v1, vector<int>v2){
        if(v1[1]<v2[1] || (v1[1]==v2[1] && v1[2]<v2[2]))
            return true;
        return false;
    }
};
