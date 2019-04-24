#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/types.h>


int main(){
  pid_t pid = scanf("%d");
  srand(time(NULL) + pid);
  printf("%d",random());
}