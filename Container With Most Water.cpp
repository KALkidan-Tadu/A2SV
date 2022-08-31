class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0, j=height.size()-1;
        int max = 0;
        while(i<j){
            if(height[i]<=height[j]){
                int area = height[i]* (j-i);
                if(area>max)
                    max = area;
                i++;
            }else{
                int area = height[j]*(j-i);
                if(area>max)
                    max = area;
                j--;
            }
        }    
        return max;
    }
};
