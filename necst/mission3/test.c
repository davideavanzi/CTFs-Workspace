#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
	printf("START\n");
	execve("/bin/bash",NULL,NULL);
	printf("END\n");
}
