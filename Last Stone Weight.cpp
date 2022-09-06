class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
      priority_queue<int, vector<int>> maxheap;
      for(int i = 0; i<stones.size(); i++){
          maxheap.push(stones[i]);
      }
        while(maxheap.size()>=2){
            int a = maxheap.top();
            maxheap.pop();
            int b = maxheap.top();
            maxheap.pop();
            if(a>b){
                a -= b;
                maxheap.push(a);
            }
        }
        if(maxheap.size() == 0)
            return 0;
        return maxheap.top();
    }
};
