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
	name = "ȫ�浿";
	tel = "000-0000-0000";
}

int main() {
	string c, t, n;
	cout << "�̸��� ��ȭ��ȣ�� �Է��� �ּ���" << endl;
	Person* p = new Person[3];
	for (int i = 0; i < 3; i++) {
		cout << "���" << i + 1 << ">>";
		cin >> c >> n;
		p[i].set(c, n);
	}
	cout << "��� ����� �̸��� ";
	for (int i = 0; i < 3; i++) {
		cout << ' ' << p[i].getName();
	}
	cout << "\n��ȭ��ȣ �˻��մϴ�. �̸��� �Է��ϼ��� >>";
	cin >> t;
	for (int i = 0; i < 3; i++) {
		if(t==p[i].getName()){
			cout << "��ȭ��ȣ�� " << p[i].getTel();
		}
		else {
			continue;
		}
	}
}