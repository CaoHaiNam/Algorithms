#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int longestCommonSubsequence(string text1, string text2){
    int l1 = text1.length();
    int l2 = text2.length();

    vector <vector<int>> dp(l2, vector<int>(l1, 0));

    for (int i = 0; i < l1; i++){
        if (text2[0] == text1[i]){
            dp[0][i] = 1;
        }else if (i != 0){
            dp[0][i] = dp[0][i-1];
        }
    }

    for (int j = 0; j < l2; j++){
        if (text1[0] == text2[j]){
            dp[j][0] = 1;
        }else if (j != 0){
            dp[j][0] = dp[j-1][0];
        }
    }

    for (int i = 1; i < l2; i++){
        for (int j = 1; j < l1; j++){
            if (text2[i] == text1[j]){
                dp[i][j] = dp[i-1][j-1]+1;
            }else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    return dp[l2-1][l1-1];

}