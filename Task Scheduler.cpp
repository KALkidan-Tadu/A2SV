class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26);
        if(n==0)
            return tasks.size();
        for(char t : tasks){
            freq[t-'A'] += 1;
        }
        sort(freq.begin(), freq.end(), greater<>());
        int maxfreq = freq[0] - 1;
        int idle = maxfreq*n;
        for(int i=1; i<freq.size(); i++){
            idle -= min(maxfreq, freq[i]);
        }
        if(idle>0)
           return idle + tasks.size(); 
        return tasks.size();
    }
};
