#include <iostream>

using namespace std;

int main()
{
    int k, n1, n2;
    
    cin >> k;
    
    for(int i = 0; i < k; i++) {
        cin >> n1  >> n2;

        if(n1 < n2) cout << n1 << " " << n2 << endl;
        else cout << n2 << " " << n1 << endl;
    }

    return 0;
}