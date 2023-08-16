#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

template <typename S>
ostream& operator<<(ostream& os,
    const vector<S>& vector)
{
    // Printing all the elements
    // using <<
    for (auto element : vector) {
        os << element << " ";
    }
    return os;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> v;

    vector<int> insert_pre;

    set<vector<int>> pre;



    for (int i = 1; i <= n; i++)
        v.push_back(i);


    vector<bool> temp(v.size(), true);

    bool flag = false;

    for (int i = 0; i <m; i++) // 뒤에 false가 n-r개 채워지고 뒤에 true 가 r개 채워진다.
        temp[i] = false;

    do {
        for (int i = 0; i < v.size(); ++i) {
            if (!temp[i])
                cout <<v[i] << " ";
        }
        cout << endl;
    } while (next_permutation(temp.begin(), temp.end()));

    return 0;

}


/*

     do {

        for (int i = 0; i < m; i++) {
            if (temp[i])
            {
                insert_pre.push_back(v[i]);
                flag = true;
            }
        }

        if (flag)
        {
            cout << "do while\n";

            for (auto i : insert_pre)
            {
                cout << i << " ";
            }
            cout << "\n";
            pre.insert(insert_pre);
        }
            flag = false;
        insert_pre.clear();
    } while (next_permutation(temp.begin(), temp.end()));


    for (auto i : pre)
    {
        cout << i << "\n";
    }
*/