class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> answer(temperatures.size());
        stack<int> stack;
        for(int i=0; i<temperatures.size(); i++){
            if(!stack.empty() && temperatures[stack.top()]< temperatures[i]){
                 while(!stack.empty() && temperatures[stack.top()]< temperatures[i]){
                int index = stack.top();
                answer[index] = i - index;
                stack.pop();
            }stack.push(i);
            }
           else
               stack.push(i);
                
        }
        return answer;
    }
};
