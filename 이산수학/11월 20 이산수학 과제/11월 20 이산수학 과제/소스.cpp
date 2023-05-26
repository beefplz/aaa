#include <iostream>
using namespace std;

int main() {
	int a[10];
	int b = 0;
	cout << "크기가 10인 정수배열을 선언하고 합을 구한다\n";
	for (int i = 0; i < 10; i++) {
		cout << i + 1 << "번쨰 숫자 입력";
		cin >> a[i];
	}
	for (int i = 0; i < 10; i++) {
		b += a[i];
	}
	cout << b << endl;
	b = 0;


	int c[3];
	cout << "3개의 정수의 합을 함수를 사용해서 구한다\n" << "정수 3개를 입력하요\n";
	for (int i = 0; i < 3; i++) {
		cin >> c[i];
	}
	for (int i = 0; i < 3; i++) {
		b += c[i];
	}
	cout << b << endl;
	b = 0;

	cout << "1~100까지 중 3의 배수의 개수를 구한다\n";
	for (int i = 1; i < 101; i++) {
		if (i % 3 == 0) {
			b += 1;
		}
		else {
			continue;
		}
	}
	cout << b << endl;
	b = 0;


	cout << "1~입력받은 정수까지의 합을 구한다\n 정수한개를 입력하세요\n";
	int f;
	cin >> f;
	for (int i = 0; i < f + 1; i++) {
		b += i;
	}
	cout << b << endl;
}