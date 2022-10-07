class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
    vector<int> seats(n);
    for (auto &b : bookings) {
        seats[b[0] - 1] += b[2];
        if (b[1] < n) 
            seats[b[1]] -= b[2];
  }
    for (auto i = 1; i < n; ++i)
        seats[i] += seats[i - 1];
    return seats;
}
};
