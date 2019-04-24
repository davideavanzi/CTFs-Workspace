#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <malloc.h>

#define RANKSIZE 10
#define CHOICEBUFSIZE 25

#define C_BLACK   "\x1b[30;0;97m"
#define C_RED     "\x1b[31m"
#define C_GREEN   "\x1b[32m"
#define C_YELLOW  "\x1b[33m"
#define C_BLUE    "\x1b[34m"
#define C_MAGENTA "\x1b[35m"
#define C_CYAN    "\x1b[36m"
#define C_WHITE   "\x1b[37;0;40m"
#define C_RESET   "\x1b[0m"

void print_black(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_BLACK, str, C_RESET);
}
void print_red(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_RED, str, C_RESET);
}
void print_green(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_GREEN, str, C_RESET);
}
void print_yellow(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_YELLOW, str, C_RESET);
}
void print_blue(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_BLUE, str, C_RESET);
}
void print_magenta(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_MAGENTA, str, C_RESET);
}
void print_cyan(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_CYAN, str, C_RESET);
}
void print_white(char *str, long long int atmp){
    printf (" [%lld] %s%s%s\n", atmp, C_WHITE, str, C_RESET);
}

typedef struct record {
    char name[368];
    long long int attempt;
    void (*print_fun)(char *, long long int);
} record;

record *ranking[RANKSIZE];

void *get_print(int c){
    switch(c){
        case 0:
        default:
            return print_black;
            break;
        case 1:
            return print_red;
            break;
        case 2:
            return print_green;
            break;
        case 3:
            return print_yellow;
            break;
        case 4:
            return print_blue;
            break;
        case 5:
            return print_magenta;
            break;
        case 6:
            return print_cyan;
            break;
        case 7:
            return print_white;
            break;
    }
    return print_black;
}

void print_rank(){
    record *r;
    int i;
    puts("*************************");
    puts("***      RANKING      ***");
    puts("*************************");
    fgets(r->name, sizeof(record)+1, stdin);

    for (i=0; i < RANKSIZE; i++){
        r = ranking[i];
        if (r == NULL){
            return;
        }
        r->print_fun(r->name, r->attempt);
    }
}

void print_color_list(){
    printf("0) %sBlack%s\n", C_BLACK, C_RESET);
    printf("1) %sRed%s\n", C_RED, C_RESET);
    printf("2) %sGreen%s\n", C_GREEN, C_RESET);
    printf("3) %sYellow%s\n", C_YELLOW, C_RESET);
    printf("4) %sBlue%s\n", C_BLUE, C_RESET);
    printf("5) %sMagenta%s\n", C_MAGENTA, C_RESET);
    printf("6) %sCyan%s\n", C_CYAN, C_RESET);
    printf("7) %sWhite%s\n", C_WHITE, C_RESET);
}

void win(long long int attempt){
    int i;
    int color;
    char buf[CHOICEBUFSIZE];
    record *r = malloc(sizeof(record));
    puts(" > You got it.\n > Are you cheating?\n");
    puts(" > I actually do not care.");
    puts(" > We have special feature.\n > Which color do you want?");
    print_color_list();
    printf(" < ");
    fgets(buf, CHOICEBUFSIZE, stdin);
    color = atoi(buf);
    r->attempt = attempt;
    r->print_fun = get_print(color);
    puts(" > what is your name?");
    printf(" < ");
    fgets(r->name, sizeof(record)+1, stdin);
    for(i=0; i < RANKSIZE; i++){
        if (ranking[i] == NULL){
            ranking[i] = r;
            break;
        }
    }
}




void play(){
    int guess=0;
    char buf[CHOICEBUFSIZE];
    long long int attempt=0;
    time_t timer;
    int value;

    time(&timer);
    timer /= 60;
    timer *= 60;

    srand(timer);
    printf(" > Hey. It is %s > What a nice day to play.\n", ctime(&timer));

    do {
        attempt += 1;
        value = rand();
        puts(" > Gimme the magic number or 0 to gtfo!");
        printf(" < ");
        fgets(buf, CHOICEBUFSIZE, stdin);
        guess = atoi(buf);
        if (guess == value){
            win(attempt);
            return;
        }
        else {
            puts(" > Not even close!\n > Try again!");
        }
    } while (guess);

}


void menu(){
    puts("1) Play");
    puts("2) Print Rank");
    puts("3) Exit");
}

int main(){
    char buf[CHOICEBUFSIZE];
    int choice;

    memset(ranking, 0, sizeof(record *) * RANKSIZE);
    while(2){
        menu();
        printf(" < ");
        fgets(buf, CHOICEBUFSIZE, stdin);
        choice = atoi(buf);
        switch (choice){
            case 1:
                play();
                // break
            case 2:
                print_rank();
                break;
            case 3:
                exit(1);
        }
    }

}
