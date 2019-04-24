#include <stdio.h>
#include <time.h>

int main(){
    time_t timer;
    time(&timer);
    timer /= 60;
    timer *= 60;
    srand(timer);
    printf("%d\n",rand());
}
