#include <stdio.h>

int main() {
    // Coordinates of points B and C
    double B_x = -6, B_y = 5;
    double C_x = -2, C_y = 3;

    // Calculate the coordinates of point A
    double A_x, A_y = 4;
    A_x = (B_x + C_x) / 2;
    
    // Find the value of a
    double a = A_x * 3;

    // Open file to write points
    FILE *file = fopen("points.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write points to the file with required formatting
    fprintf(file, "Point A: (%.2f, %.2f)\n", A_x, A_y);
    fprintf(file, "Point B: (%.2f, %.2f)\n", B_x, B_y);
    fprintf(file, "Point C: (%.2f, %.2f)\n", C_x, C_y);

    // Close the file
    fclose(file);

    // Output value of a to console
    printf("Calculated value of a: %.2f\n", a);
    printf("Points have been saved to points.txt\n");

    return 0;
}

