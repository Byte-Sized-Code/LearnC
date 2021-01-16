/*
Given the size and the elements of array A, print all the elements in reverse order.

Input:
First line of input contains, N - size of the array.
Following N lines, each contains one integer, i{th} element of the array i.e. A[i].

Output:
Print all the elements of the array in reverse order, each element in a new line.
*/

// Header to include the io library
#include <stdio.h>

// Main function that is called when the file is executed
int main()
{
  // size of array
	int N;
	scanf("%d", &N);  // reading size of array

  // initialize array
  int arr[N];
  // read values and add to array
	for (int inp=0; inp<N; inp++)
	{
		int n;
		scanf("%d", &n);
		arr[inp] = n;
	}

  // read array in reverse order and print values
	for (int idx=N-1; idx>-1; idx--)
	{
		printf("%d\n", arr[idx]);  // writing output
	}
}
