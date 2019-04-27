#include <stdio.h>

int main(){
    unsigned int random = rand();
    printf("%d\n", random ^ 0xdeadbeef);
}
