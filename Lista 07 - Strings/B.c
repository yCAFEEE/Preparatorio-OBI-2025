#include <stdio.h>
#include <string.h>

int main(){
    char str1[1001], str2[1001];
    scanf("%s %s", str1, str2);

    int cord_str1 = -1, cord_str2 = -1; 
    for(int i = 0; str1[i] != '\0'; i++){
        for(int j = 0; str2[j] != '\0'; j++){
            if(str1[i] == str2[j]){
                cord_str1 = i + 1;
                cord_str2 = j + 1;
            }
        }
    }

    printf("%d %d\n", cord_str1, cord_str2);

    return 0;
}

//🗣 esse código faz exatamente a mesma coisa que o B.py, mas em python ele não funciona (TLE) e em C funciona 🔥