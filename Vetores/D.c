#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
    int n;
    scanf("%d", &n);
    int *v = malloc(sizeof(int) * n);
    for(int i = 0; i < n; i++){
        scanf("%d", &v[i]);
    }

    bool possivel = true;
    for(int i = 0; i < n-1; i++){
        if(v[0] > 8){
            possivel = false;
            break;
        }
        if((v[i+1] - v[i]) > 8){
            possivel = false;
            break;
        }
    }
    printf("%s\n", possivel ? "S" : "N");
}