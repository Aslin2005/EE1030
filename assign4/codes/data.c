#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int a, b;
    srand(time(NULL));
      a = rand() % 10; 
    b = rand() % 10;
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file for writing.\n");
        return 1;
    }
    fprintf(file, "a = %d\n", a);
    fprintf(file, "b = %d\n", b);

    fclose(file);

    printf("Values of a and b have been written to data.tex\n");

    return 0;
}

