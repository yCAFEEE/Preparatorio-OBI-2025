#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int id_pessoa[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &id_pessoa[i]);
    }

    int m;
    scanf("%d", &m);
    int id_pessoa_sai[m];
    for(int i = 0; i < m; i++){
        scanf("%d", &id_pessoa_sai[i]);
    }

    int id_pessoa_restante[n-m];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(id_pessoa[i] == id_pessoa_sai[j]){
                continue;
            }else{
                id_pessoa_restante[i] = id_pessoa[i];
            }
        }
    }

    for(int i = 0; i < n-m; i++){
        printf("%d ", id_pessoa_restante[i]);
    }
    printf("\n");
    return 0;
}