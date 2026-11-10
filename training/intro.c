/* Benign exercise: inspect this control flow in a disassembler.
 * Compile only this reviewed source, not an unknown sample.
 * Example inside your development VM: cc -O0 -g intro.c -o intro
 */
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        puts("Provide one word.");
        return 1;
    }
    if (strcmp(argv[1], "curiosity") == 0) {
        puts("Keep learning.");
    } else {
        puts("Try another word.");
    }
    return 0;
}
