// 1546 / Average

#include <iostream>
using namespace std;

int main() {

	int n, max;    // 과목 수 입력받을 변수
	long double total = 0;    // total값 초기화

	cin >> n;    // 과목 수 입력받기

	long double* q = new long double[n];    // 과목 수 만큼 공간 할당

	// 점수 입력받기
	for (int i = 0; i < n; i++) {
		cin >> q[i];
		max = q[0];
	}

	for (int i = 0; i < n; i++) {
		if (q[i] > max)
			max = q[i];
	}

	// 계산식
	for (int i = 0; i < n; i++) {
		q[i] = q[i] / max * 100;
		total += q[i];
	}

	total /= n;

	cout << total;

	delete[]q;
}