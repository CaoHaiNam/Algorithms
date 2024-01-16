#include <iostream>
#include <vector>
#include <unordered_set>
#include <cstdlib> // For rand and srand
#include <ctime> // For time
using namespace std;

class RandomizedSet{
private:
    vector<int> vec;
    unordered_set<int> set;

public:
    RandomizedSet(){
        // Seed the random number generator
        std::srand(std::time(0));
    }

    bool insert(int val){
        if (set.count(val) > 0){
            return false;
        }
        vec.push_back(val);
        set.insert(val);
        return true;
    }

    bool remove(int val){
        if (set.count(val) > 0){
            vec.erase(std::remove(vec.begin(), vec.end(), val), vec.end());
            set.erase(val);
            return true;
        }
        return false;
    }
    
    int getRandom(){
        if (!vec.empty()){
            int randomIndex = std::rand()%vec.size();
            return vec[randomIndex];
        }
        return -1;
    }
};

int main() {
    // Example usage
    RandomizedSet randomizedSet;

    randomizedSet.insert(1);
    randomizedSet.insert(2);
    randomizedSet.insert(3);

    std::cout << "Random element: " << randomizedSet.getRandom() << std::endl;

    randomizedSet.remove(2);

    std::cout << "Random element after removal: " << randomizedSet.getRandom() << std::endl;

    return 0;
}
