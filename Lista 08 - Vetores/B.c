#include <stdio.h>

int main(){
    int cont = 0, aposta[6], sorteados[6];
    for(int i = 0; i < 6; i++){
        scanf("%d", &aposta[i]);
    }
    for(int i = 0; i < 6; i++){
        scanf("%d", &sorteados[i]);
    }
    for(int i = 0; i < 6; i++){
        for(int j = 0; j < 6; j++){
            if(aposta[i] == sorteados[j]){
                cont++;
            }
        }
    }
    if(cont == 3) printf("terno\n");
    if(cont == 4) printf("quadra\n");
    if(cont == 5) printf("quina\n");
    if(cont == 6) printf("sena\n");
    if(cont < 3) printf("azar\n");
}