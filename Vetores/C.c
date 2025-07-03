#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d", &n);
    int *v = malloc(sizeof(int) * n);

    for(int i = 0; i < n; i++){
        scanf("%d", &v[i]);
    }
    int picoDuplo = 0;
    for(int i = 1; i < n - 1; i++){
        if(v[i] < v[i-1] && v[i] < v[i+1]){
            picoDuplo = 1;
            break;
        }
    }
    printf("%s\n", picoDuplo ? "S" : "N");
    free(v);
    return 0;
}