int read(int fd, char *buf, int size){
    int res;
    asm ("mov $3, %%eax\n\t"
         "int $128\n\t"
        : "=a" (res)
         : "b" (fd), "c" (buf), "d" (size)
         );
    return res;
}

int write(int fd, char *buf, int size){
    int res;
    asm ("mov $4, %%eax\n\t"
         "int $128\n\t"
         : "=a" (res)
         : "b" (fd), "c" (buf), "d" (size)
         );
    return res;
}

void exit(int code){
    asm ("mov $1, %%eax\n\t"
         "int $128"
         :
         : "b" (code)
         );
}


#define MTDO "Try easyROP!\n"

long long len = 0;
int index = 0;

// Do you know that there are some tools to find gadgets ? :P

int main() {
    int array[48];
    int a, b;
    len = 0xc3585B595A;
    write(1, MTDO, 13);
    while(len > 2) {
        len = 0;
        len += read(0, &a, 4);
        len += read(0, &b, 4);
        array[index++] = a + b;
        write(1,&len, 4);
    }

}

int _start() {
    main();
    exit(0);
}
