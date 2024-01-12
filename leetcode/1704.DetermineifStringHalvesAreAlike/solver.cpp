#include <iostream>
#include <unordered_set>
using namespace std;

int countVowels(const string& s){
    // unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    unordered_set <char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        
    // unordered_set<char> vowels;
    // vowels.insert({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'});

    // unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    int count = 0;

    for (int i = 0; i < s.length(); i++){
        if (vowels.count(s[i]) > 0){
            count ++;
        }
    }

    return count;
}

bool halvesAreAlike(string s){
    int n = s.length();
    int countA = countVowels(s.substr(0, n / 2));
    int countB = countVowels(s.substr(n/2));

    return countA == countB;
}

int main() {
    // Example usage:
    string input = "AbCdEfGh";
    bool result = halvesAreAlike(input);
    
    // Output the result
    cout << (result ? "true" : "false") << endl;

    return 0;
}