#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

const char *words[] = {
  "blockchain",
  "cyber",
  "fuzzing",
  "symbolic",
  "deep",
  "convolutional",
  "automatic",
  "monadic",
  "memory-safe",
  "airgannon",
  "state-transactional"
};

int canary;

void vuln() {
  struct {
    char estimated[128];
    int real;
    int canary;
  } local;

  canary = random();
  local.canary = canary;

  fputs("Q: What is the estimated market value of\n   ", stdout);
  for (int i=0; i<(random() % 6) + 1; i++) {
    fputs(words[random() % (sizeof(words) / sizeof(words[0]))], stdout);
    putchar(' ');
  }
  printf("software\n   going to be in %ld?\n\nA: ", 2020 + (random() % 100));
  fflush(stdout);

  local.real = random();
  scanf("%s", local.estimated);

  if (local.canary != canary) {
    puts("\n\n:'( PLS DO NOT CHEAT U MAKE ME CRY SALTY TEARS :'(\n\n");
    exit(0);
  }

  int estimated = atoi(local.estimated);

  fputs("\nAnd the right answer is... ", stdout);
  if (estimated == local.real) {
    printf(local.estimated);
  } else {
    printf("%d", local.real);
  }

  puts("\n\nBYE!");
}

int main(int argc, char **argv) {
  srand(time(NULL) + getpid());

  puts("");
  puts("+==========================================================================+");
  puts("|                        WELCOME TO THE NEW HIT SHOW                       |");
  puts("+==========================================================================+");
  puts("|                                Programmers,                              |");
  puts("|                             what do they know?                           |");
  puts("|                           do they know things?                           |");
  puts("|                              Let's find out!                             |");
  puts("+==========================================================================+");
  puts("");

  vuln();

  return 0;
}

