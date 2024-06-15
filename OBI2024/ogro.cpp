#include <bits/stdc++.h>

using namespace std;

int main() {
    int e, d;
    cin >> e;
    cin >> d;
    
    if(e > d) {
        cout << e + d << endl;
    } else {
        int g = 2 * (d - e);
        cout << g << endl;
    }
}