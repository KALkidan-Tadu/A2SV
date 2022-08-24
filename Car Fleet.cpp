class Solution {
public:
    struct Car {
       int pos;
       double time;  
    };
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<Car> cars(speed.size());
        int fleet = 0;
        for (int i = 0; i < position.size(); ++i)
              cars[i] = {position[i], (double)(target - position[i]) / speed[i]};
        sort(begin(cars), end(cars),
         [](const auto& a, const auto& b) { return a.pos > b.pos; });
        double max = 0;
        for (const auto& car : cars){
            if (car.time > max) {
                max = car.time;
                fleet++;
      }
        }
      return fleet;
    }
};
