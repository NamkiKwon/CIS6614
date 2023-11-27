#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str;
    cout << "Please enter your string: \n";
    getline(cin, str);
    unsigned int len = str.length();
    if (len > -1)
    {
    cout << "string length is " << len << "which is bigger than -1 " <<std::endl;
    }else 
    {
    cout << "string length is " << len << " which is less than -1 " <<std::endl;
    }
    return 0;
}
