#include <stdio.h>

int main(){
    int v[5], trofeu = 1, placa = 0, segundo = -1;
    for(int i = 0; i < 5; i++){
        scanf("%d", &v[i]);
    }
    for(int i = 0; i < 4; i++){
        if(v[0] == v[i + 1]){
            trofeu++;
        }
    }
    for(int i = 0; i < 5; i++){
        if(v[i] < v[0] && v[i] > segundo){
            segundo = v[i];
        }
    }
    for(int i = 0; i < 5; i++){
        if(v[i] == segundo){
            placa++;
        }
    }

    printf("%d %d\n", trofeu, placa);
}