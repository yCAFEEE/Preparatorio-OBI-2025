#include <stdio.h>

int main(){
    int p, d, b;
    scanf("%d", &p);
    scanf("%d", &d);
    scanf("%d", &b);
    int s_pontos = p + (d * 2) + (b * 3);
    if(s_pontos >= 150){
        printf("B\n");
    }else if(s_pontos < 150 && s_pontos >= 120){
        printf("D\n");
    }else if(s_pontos < 120 && s_pontos >= 100){
        printf("P\n");
    }else{
        printf("N\n");
    }
}