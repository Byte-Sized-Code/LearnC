// Given a 2D array A, your task is to convert all rows to columns and columns to rows.
//
// Input:
// First line contains 2 space separated integers, N - total rows, M - total columns.
// Each of the next N lines will contain M space separated integers.
//
// Output:
// Print M lines each containing N space separated integers.

// header for standard io
#include <stdio.h>

// main function
int main(){
	int N, M;
	scanf("%d", &N);
	scanf("%d", &M);
	int arr[N][M];
  // filling the array
	for (int i=0; i<N; i++){
		for (int j=0; j<M; j++){
			int val;
			scanf("%d", &val);
			arr[i][j] = val;
		}
	}
  // printing the transpose of array
	for (int i=0; i<M; i++){
		for (int j=0; j<N; j++){
			printf("%d ", arr[j][i]);
		}
		printf("\n");
	}
}
