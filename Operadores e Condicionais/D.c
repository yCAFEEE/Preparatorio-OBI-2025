#include <stdio.h>

int main(){
    int idade1, idade2, preco1, preco2;
    scanf("%d", &idade1);
    scanf("%d", &idade2);
    if(idade1 <= 17){
        preco1 = 15;
    }
    if(idade2 <= 17){
        preco2 = 15;
    }
    if(idade1 >= 18 && idade1 <= 59){
        preco1 = 30;
    }
    if(idade2 >= 18 && idade2 <= 59){
        preco2 = 30;
    }
    if(idade1 >= 60){
        preco1 = 20;
    }
    if(idade2 >= 60){
        preco2 = 20;
    }
    printf("%d\n", preco1 + preco2);
    return 0;
}