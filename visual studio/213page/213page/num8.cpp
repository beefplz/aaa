#include <iostream>
using namespace std;

class Circle {
	int radius;
public:
	Circle();
	void setradius(int r) { radius = r; }
	double getArea() { return 3.14 * radius * radius; }
};

Circle::Circle() {
	radius = 1;
}

int main() {
	int c;
	int radius;
	int num;
	int a = 0;
	cout << "���� ���� �Է� >>";
	cin >> num;
	Circle* p = new Circle[num];
	for (int i = 0; i < num; i++) {
		cout << "��" << i+1 << "�� �������� ũ�� <<";
		cin >> c;
		p[i].setradius(c);
	}
	for (int i = 0; i < num; i++) {
		if (p[i].getArea() > 100) {
			a++;
		}
	}
	cout << "������ 100���� ū ����" << a << "�� �Դϴ�";
}