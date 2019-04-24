// Note that this executable is compiled for x86_64 (64 bit)
// Try to grab a shell -- and this time, you can't overwrite the $RIP!

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

struct guess_s
{
	long val;
	long super_secret_value;
	char input[16];
};

char flag[896];

unsigned int getNumber()
{
	struct guess_s guess;

    read(0, guess.input, 0x16); // 0X16 = 22 = 16 + 6 != 16 I CAN overvrite super_secret_value but it's useless. NOP i can overwrite the 6 lower byts of the ebp!
    guess.val = atoi(guess.input);
    memset(guess.input, 0, 16);
    return guess.val;
}

unsigned int guessNumber()
{
	uint max_val = UINT_MAX;

    printf("Nope. I'll give you one more chance.\n");
    printf("Guess the number i'm thinking between 0 and %u.\n", max_val);
    return getNumber();
}

void getString(char* input, size_t max)
{
    size_t size;

    size = read(0, input, max);
    input[max - 1] = 0;
    if(input[size - 1] == '\n')
    {
        input[size - 1] = 0;
    }
}

int checkAuth()
{
    char username[56];
    char password[896];
    int fd;
    uint random_number;

    printf("username: ");
    getString(username, 56);
    if(!strcmp(username, "admin"))
    {   
    	memset(username, 0, 56);
        printf("That was easy, and now?\n");
        printf("password: ");
        getString(password, 896);
        if(!strcmp(password, flag))
        {
            printf("Welcome back admin!\n");
            return 0xDEADBEEF;
        }
        else
        {
        	printf("Wrong password\n");
        	memset(password, 0, 896);
        	fd = open("/dev/urandom", O_RDONLY);
        	read(fd, &random_number, 4);
            if(random_number == guessNumber())
            {
                printf("I really hope you didn't guessed it.\n");
                return 0xDEADBEEF;
            }
            else
            {
            	printf("Nope.\n");
            }
        }
    }
    else
    {
        printf("Cmon dude! The username is admin, is always admin!!!\n");
        printf("It's called SECURE shell authenication, if it's not admin what it should be?!\n");
    }
    return 0;
}

int main(int argc, char const *argv[])
{

    FILE *fp;

    // Init stuffs
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
    //

    puts("#################################################");
    puts("########## SECURE SHELL AUTHENTICATION ##########");
    puts("#################################################");
    fp = fopen("./flag", "r");
    if(fp == NULL)
    {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }
    fgets(flag, 896, fp);
    if(flag == NULL)
    {
        perror("Memory allocation error.\n");
        exit(EXIT_FAILURE);
    }
    flag[896 - 1] = 0;
    if(checkAuth() == 0xDEADBEEF)
    {
        system("/bin/sh");
    }
    return 0;
}