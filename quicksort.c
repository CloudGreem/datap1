// quicksort_submit.c
// 사용법(입력 형식):
//   첫 줄에 정수 n
//   둘째 줄에 정수 n개 (공백 구분)
// 출력:
//   정렬된 수열을 표준출력(화면)과 output.txt 파일에 기록

#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) { int t = *a; *a = *b; *b = t; }


int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) { ++i; swap(&arr[i], &arr[j]); }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// 퀵소트 
void quickSort(int * array, int low, int high) {
    if (low < high) {
        int pi = partition(array, low, high);
        quickSort(array, low, pi - 1);
        quickSort(array, pi + 1, high);
    }
}

// 배열을 지정한 스트림으로 출력
void printArrayTo(FILE *out, const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        if (i) fprintf(out, " ");
        fprintf(out, "%d", arr[i]);
    }
    fprintf(out, "\n");
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 0) {
        fprintf(stderr, "입력 오류 : n이 올바르지 않습니다.\n");
        return 1;
    }

    int *arr = (int*)malloc(sizeof(int) * (size_t)n);
    if (!arr) {
        fprintf(stderr, "메모리 할당 실패\n");
        return 1;
    }

    for (int i = 0; i < n; ++i) {
        if (scanf("%d", &arr[i]) != 1) {
            fprintf(stderr, "입력 오류\n");
            free(arr);
            return 1;
        }
    }

    if (n > 1) quickSort(arr, 0, n - 1);

    // 화면 출력 
    printArrayTo(stdout, arr, n);

    // 파일 출력 
    FILE *fp = fopen("output.txt", "w");
    if (!fp) {
        fprintf(stderr, "파일 열기 실패: output.txt\n");
        free(arr);
        return 1;
    }
    printArrayTo(fp, arr, n);
    fclose(fp);

    free(arr);
    return 0;
}
