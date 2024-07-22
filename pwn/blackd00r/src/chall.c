#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

unsigned long long key = 0xdeadbeef;
int blackd00r() {
    if (key == 0xbabec0fe) {
        puts("You got it!");
        system("/bin/cat flag.txt");
    }
    return 0;
}

int vuln(){
    char v4[4];
    char v5[4]; 
    char v6[16]; 
    puts("Harry left a exploit function, can you find it?");
    gets(v6); 
    memcpy(*(int*)v4,*(int*)v5,sizeof(int));
}

int main() {
    setvbuf(stdin, 0, 2, 0); 
    setvbuf(stdout, 0, 2, 0); 
    fflush(stdout);
    vuln();
    return 0;
}
