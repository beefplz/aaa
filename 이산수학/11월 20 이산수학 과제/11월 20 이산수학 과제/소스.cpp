#include <iostream>
using namespace std;

int main() {
	int a[10];
	int b = 0;
	cout << "ũ�Ⱑ 10�� �����迭�� �����ϰ� ���� ���Ѵ�\n";
	for (int i = 0; i < 10; i++) {
		cout << i + 1 << "���� ���� �Է�";
		cin >> a[i];
	}
	for (int i = 0; i < 10; i++) {
		b += a[i];
	}
	cout << b << endl;
	b = 0;


	int c[3];
	cout << "3���� ������ ���� �Լ��� ����ؼ� ���Ѵ�\n" << "���� 3���� �Է��Ͽ�\n";
	for (int i = 0; i < 3; i++) {
		cin >> c[i];
	}
	for (int i = 0; i < 3; i++) {
		b += c[i];
	}
	cout << b << endl;
	b = 0;

	cout << "1~100���� �� 3�� ����� ������ ���Ѵ�\n";
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


	cout << "1~�Է¹��� ���������� ���� ���Ѵ�\n �����Ѱ��� �Է��ϼ���\n";
	int f;
	cin >> f;
	for (int i = 0; i < f + 1; i++) {
		b += i;
	}
	cout << b << endl;
}