#include <bits/stdc++.h>
using namespace std;


bool isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}


string encryptMessage(const string &message) {
    string encrypted;
    for (char ch : message) {
        int shift = isVowel(ch) ? 1 : 2;
        char newChar = 'a' + (ch - 'a' + shift) % 26;
        encrypted += newChar;
    }
    return encrypted;
}

int main() {
    string message;
    cin >> message;
    cout << encryptMessage(message) << endl;
    return 0;
}
