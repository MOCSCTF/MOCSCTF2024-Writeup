#include <stdio.h>

int main(void)
{
	char buf[4096];

	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
	while (1) {
		read(0, buf, sizeof(buf));
		printf(buf);
	}
}

