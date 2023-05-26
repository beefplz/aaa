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
	cout << "원의 개수 입력 >>";
	cin >> num;
	Circle* p = new Circle[num];
	for (int i = 0; i < num; i++) {
		cout << "원" << i+1 << "의 반지름의 크기 <<";
		cin >> c;
		p[i].setradius(c);
	}
	for (int i = 0; i < num; i++) {
		if (p[i].getArea() > 100) {
			a++;
		}
	}
	cout << "면적이 100보다 큰 원은" << a << "개 입니다";
}