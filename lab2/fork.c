#include <stdio.h>
#include <unistd.h>
/* This program forks and and the prints whether the process is
 *   - the child (the return value of fork() is 0), or
 *   - the parent (the return value of fork() is not zero)
 *
 * When this was run 100 times on the computer the author is
 * on, only twice did the parent process execute before the
 * child process executed.
 *
 * Note, if you juxtapose two strings, the compiler automatically
 * concatenates the two, e.g., "Hello " "world!"
 */

int main(int argc, char *argv[]) {
	int pid = fork();

	if ( pid == 0 ) {
		printf( "This is being printed from the child process\n" );
	} else {
		printf( "This is being printed in the parent process:\n"
		        " - the process identifier (pid) of the child is %d\n", pid );
	}
	return 0;
}
