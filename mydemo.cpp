#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int n;
    while (true)
    {
        cout << "请输入数字：";
        cin >> n;
        if (n > 100)
        {
            cout << "请输入小于100的数字";
            continue;
        }

        for (; n <= 100; n++)
        {
            cout<<n<<endl;
        }
        break;
    }

    getchar();
    return 0;
}