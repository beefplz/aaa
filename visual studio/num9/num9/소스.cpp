#include <iostream>
using namespace std;

class Person {
	string name;
	string tel;
public:
	Person();
	string getName() { return name; }
	string getTel() { return tel; }
	void set(string n, string t) { name = n, tel = t; }
};

Person::Person() {
	name = "홍길동";
	tel = "000-0000-0000";
}

int main() {
	string c, t, n;
	cout << "이름과 전화번호를 입력해 주세요" << endl;
	Person* p = new Person[3];
	for (int i = 0; i < 3; i++) {
		cout << "사람" << i + 1 << ">>";
		cin >> c >> n;
		p[i].set(c, n);
	}
	cout << "모든 사람의 이름은 ";
	for (int i = 0; i < 3; i++) {
		cout << ' ' << p[i].getName();
	}
	cout << "\n전화번호 검색합니다. 이름을 입력하세요 >>";
	cin >> t;
	for (int i = 0; i < 3; i++) {
		if(t==p[i].getName()){
			cout << "전화번호는 " << p[i].getTel();
		}
		else {
			continue;
		}
	}
}