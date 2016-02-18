#include <stdio.h>

int merge(int A[], int p, int q, int r) {
    int i, j, k, inversions = 0;

    int n1 = q - p + 1;
    int n2 = r - q;

    int L[n1];
    int R[n2];

    for (i = 0; i < n1; i++) L[i] = A[p + i];
    for (j = 0; j < n2; j++) R[j] = A[q + j + 1];

    for(i = 0, j = 0, k = p; k <= r; k++) {
        if (i == n1) {
            A[k] = R[j++];
        } else if (j == n2) {
            A[k] = L[i++];
        } else if (L[i] <= R[j]) {
            A[k] = L[i++];
        } else {
            A[k] = R[j++];
            inversions += n1 - i;
        }
    }

    return inversions;
}

int merge_sort(int A[], int p, int r) {
    if (p < r) {
        int inversions = 0;
        int q = (p + r) / 2;
        inversions += merge_sort(A, p, q);
        inversions += merge_sort(A, q + 1, r);
        inversions += merge(A, p, q, r);
        return inversions;
    } else {
        return 0;
    }
}

int main(){
    int A[] = {1,3,5,7,9, 2,4,6,8,10}
    printf("%d", merge_sort(A, 0, 9));
}

