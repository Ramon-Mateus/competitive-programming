#include <bits/stdc++.h>
#include <string>
#include <cmath>

using namespace std;

int main()
{
  int a, b, c;

  cin >> a >> b >> c;

  vector<int> entrada = { a, b, c };

  sort(entrada.begin(), entrada.end());

  if(entrada[2] == 2) {
    cout << "3" << endl;
  } else {
    if (entrada[1] == 1)
    {
      cout << "2" << endl;
    } else {
      cout << "1" << endl;
    }
  }
}