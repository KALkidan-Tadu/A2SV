class Solution {
public:
    long long div = pow(10,9)+7;
    long long power(long long a, long long b){
        if(b==0)
            return 1;
        long long answer = power(a, b/2);
        if(b%2 == 0)
            return (answer*answer)%div;
        return (((answer*answer)%div) * (a%div))%div;
    }
    int minNonZeroProduct(int p) {
        long long maxim = pow(2,p);
        long long maximum = maxim-1;
        long long result = power((maximum-1), ((maximum-1)/2));
        return (result*(maximum%div))%div;
    }
};
