#include <stdio.h>

int main(){
    int Cv, Ce, Cs, Fv, Fe, Fs;

    scanf("%d %d %d %d %d %d", &Cv, &Ce, &Cs, &Fv, &Fe, &Fs);

    int pontuaC = (Cv * 3) + Ce;
    int pontuaF = (Fv * 3) + Fe;

    if(pontuaC == pontuaF){
        if(Cs > Fs){
            printf("C\n");
        }else if(Cs < Fs){
            printf("F\n");
        }else{
            printf("=\n");
        }
        return 0;
    }

    if(pontuaC > pontuaF){
        printf("C\n");
    }else{
        printf("F\n");
    }

    return 0;
}