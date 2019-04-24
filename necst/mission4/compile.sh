#!/bin/bash
gcc -m32 -no-pie -fno-stack-protector -z execstack -o mission4 mission4.c