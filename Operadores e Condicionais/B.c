#include <stdio.h>

int main(){
    int e, d;
    scanf("%d", &e);
    scanf("%d", &d);
    if(e > d){
        printf("%d\n", e + d);
    }else{
        printf("%d\n", 2 * (d - e));
    }
}