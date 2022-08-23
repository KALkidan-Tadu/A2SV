class Solution {
public:
int optimal(vector<int>& nums, int i, int j) {
if(i > j) {
return 0;
}

    int ans1=nums[i]+min(optimal(nums, i+2, j), optimal(nums, i+1, j-1)); 
    int ans2=nums[j]+min(optimal(nums, i+1, j-1), optimal(nums, i, j-2)); 
    
    return max(ans1, ans2); 
} 

bool PredictTheWinner(vector<int>& nums) { 
    int n=nums.size(); 
    
    if(n == 1) {
        return true; 
    }
    
    int total=0; 
    for(int i=0; i<n; i++) {
        total = total + nums[i]; 
    } 
    
    int player1=optimal(nums, 0, n-1); 
    int player2=total-player1; 
    
    if(player1 < player2) {
        return false; 
    } 
    return true; 
}
};
