#include<iostream>
#include<vector>
using namespace std;

class MyQueue{
private:
    vector<int> queue;

public:
    MyQueue(){}

    void push(int x){
        queue.push_back(x);
    }

    int pop(){
        if (!queue.empty()){
            int x = queue[0];
            queue.erase(queue.begin());
            return x;
        }
        return -1;
    }

    int peek(){
        if (!queue.empty()){
            return queue[0];
        }
        return -1;
    }

    bool empty(){
        return queue.empty();
    }
};