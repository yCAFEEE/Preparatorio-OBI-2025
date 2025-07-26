#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int v[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &v[i]);
    }

    while(n > 1){
        int aux[n - 1];
        for(int i = 0; i <  n - 1; i++){
            if(v[i] == v[i + 1]){
                aux[i] = -1;
            }else{
                aux[i] = 1;
            }
        }
        for(int i = 0; i < n - 1; i++){
            v[i] = aux[i];
        }
        n--;
    }
    if(v[0] == 1){
        printf("branca\n");
    }else{
        printf("preta\n");
    }
}