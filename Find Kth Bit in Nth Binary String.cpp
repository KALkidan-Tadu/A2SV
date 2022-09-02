class Solution {
public:
    char findKthBit(int n, int k) {
        if(n==1 && k==1)
            return '0';
        int p = pow(2,n);
        int mid = p/2;
        if(k==mid)
            return '1';
        if(k<mid)
            return findKthBit(n-1, k);
        char answer = findKthBit(n-1, p-k);
        if(answer == '0')
            return '1';
        return '0';
    }
};
