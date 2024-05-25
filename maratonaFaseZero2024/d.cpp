#include <bits/stdc++.h>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int e, v;

    cin >> e >> v;

    double div = double(e) / double(v);

    double horas;

    double minutos = modf(div, &horas);

    minutos = (minutos * 60);

    if(floor(minutos) == 60) {
        minutos = 0;
        horas += 1;
    }

    long long int horaFinal = int(horas + 19) % 24;

    cout << setw(2) << setfill('0') << horaFinal << ":" << setw(2) << setfill('0') << floor(minutos) << endl;
}