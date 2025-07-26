#include <stdio.h>

int main(){
    int d, a, n, diaria;
    scanf("%d", &d);
    scanf("%d", &a);
    scanf("%d", &n);

    if(n <= 15){
        diaria = (32-n) * (d + (n-1) * a);
    }else{
        diaria = (32-n) * (d + 14 * a);
    }
    printf("%d\n", diaria);
    return 0;
}