#include <stdio.h>

int main(){
    int n;
    int max = -1;
    while(n != 0){
        scanf("%d", &n);
        if(n > max){
            max = n;
        }
    }

    printf("%d\n", max);

    return 0;
}