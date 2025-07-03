#include <stdio.h>
#include <stdlib.h>

void merge(int *v, int *v1, int *v2, int *pos, int *pos1, int *pos2, size_t size){
    size_t size_v1 = size / 2;
    size_t size_v2 = size - size_v1;
    int i = 0, j = 0, k = 0;
    for(i; j < size_v1 && k < size_v2; i++){
        if(v1[j] <= v2[k]){
            v[i] = v1[j];
            pos[i] = pos1[j];
            j++;
        }else{
            v[i] = v2[k];
            pos[i] = pos2[k];
            k++;
        }
    }
    while(j < size_v1){
        v[i] = v1[j];
        pos[i] = pos1[j];
        i++;
        j++;
    }
    while(k < size_v2){
        v[i] = v2[k];
        pos[i] = pos2[k];
        i++;
        k++;
    }
}

void merge_sort(int *v, int *pos, size_t size){
    size_t mid = size / 2;
    if(size > 1){
        int *v1 = malloc(sizeof(int) * size);
        int *v2 = malloc(sizeof(int) * (size - mid));
        int *pos1 = malloc(sizeof(int) * size);
        int *pos2 = malloc(sizeof(int) * (size - mid));

        for(int i = 0; i < mid; i++){
            v1[i] = v[i];
            pos1[i] = pos[i];
        }
        for(int i = mid; i < size; i++){
            v2[i - mid] = v[i];
            pos2[i - mid] = pos[i];
        }
        merge_sort(v1, pos1, mid);
        merge_sort(v2, pos2, size - mid);
        merge(v, v1, v2, pos, pos1, pos2, size);
        free(v1);
        free(v2);
        free(pos1);
        free(pos2);
    }
}
int main(){
    int n;
    scanf("%d", &n);
    int v[n], pos[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &v[i]);
        pos[i] = i + 1;
    }
    merge_sort(v, pos, n);
    for(int i = 0; i < n; i++){
        printf("%d\n", pos[i]);
    }
}