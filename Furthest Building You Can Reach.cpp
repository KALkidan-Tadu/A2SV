class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int i;
        priority_queue<int> q;
       for(i=0; i<heights.size()-1; i++){
           if(heights[i+1] > heights[i]){
               int jump = heights[i+1] - heights[i];
               if(bricks>=jump){
                   bricks -= jump;
                   q.push(jump);
               }else if(ladders > 0){
                   if(q.size()>0){
                       if(q.top()>jump){
                       bricks+=q.top();
                       q.pop();
                       q.push(jump);
                       bricks-= jump;
                   }
                   }
                       ladders--;
               }else 
                   break;
           }
       } 
        return i;
    }
};
