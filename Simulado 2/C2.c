#include <stdio.h>

int main(){
    int n;
    int max = -1;
    for(int i = 0; i <= 100; i++){
        scanf("%d", &n);
        if(n == 0) break;
        if(n > max) max = n;
    }

    printf("%d\n", max);

    return 0;
}