#include <stdio.h>

int main() {
    // Define the points
    float A[] = {0.0, 0.0};
    float B[] = {4.8, 0.0};
    float C[] = {2.81, 2.45};

    // Open the file for writing
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the points to the file
    fprintf(file, "(%.2f,%.2f)\n", A[0], A[1]);
    fprintf(file, "(%.2f,%.2f)\n", B[0], B[1]);
    fprintf(file, "(%.2f,%.2f)\n", C[0], C[1]);

    // Close the file
    fclose(file);
    
    printf("Data written to data.txt successfully.\n");
    return 0;
}

