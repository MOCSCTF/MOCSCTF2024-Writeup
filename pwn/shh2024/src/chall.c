#include <stdio.h>
#include <unistd.h>

char talk[8];
char secret[4];

void run() {
    printf("shhhhhh!!!!!\n");
    system("echo 'shhhhhh!!'");
    exit(0);
}

void talking() {
    printf("tell me something\n");
    read(0, talk, 256);
    return;
}

void setup_canary() {
FILE *file = fopen("canary.txt", "r");
if (file == NULL) {
    printf("Failed to open canary.txt\n");
    exit(-1);
}
fread(secret,sizeof(char),4,file);
fclose(file);
}


void vuln() { 
    char canary[4];
    char buf[16];
   
    memcpy(canary,secret,4);
    read(0, buf, 256);
    if (memcmp(canary,secret,4)) {
      printf("shhhhh... what is my secret\n");
      exit(-1);
   }
   printf("shhhh!! keep in secret..\n");
    return;
}

int main(void) {

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL); 

    printf("SSH-99.99-OpenSHH_MK34 Ubuntu-3ubuntu3.3\n");
    printf("Hell....Hel....He...H.........\n");
    setup_canary();
    vuln();
}
