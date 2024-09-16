#include <stdio.h>
#include <stdlib.h>

int main() {
    int a = 8;
    int b = 9;

    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file for writing.\n");
        return 1;
    }

    fprintf(file, "a = %d\n", a);
    fprintf(file, "b = %d\n", b);

    fclose(file);

    printf("Values of a and b have been written to data.txt\n");

    return 0;
}

