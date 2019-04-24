#include <stdio.h>

int main(){
    FILE *fp = fopen("flag", "r");
    char c = fgetc(fp); 
    while (c != EOF) 
    { 
        printf ("%c", c); 
        c = fgetc(fp); 
    } 
}

