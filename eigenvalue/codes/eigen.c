#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int n;

    printf("Enter the size of the matrix (n): ");
    scanf("%d", &n);

    double** A = (double**)malloc(n * sizeof(double*));
    double** E = (double**)malloc(n * sizeof(double*));
    double** V = (double**)malloc(n * sizeof(double*));

    for (int i = 0; i < n; i++) {
        A[i] = (double*)malloc(n * sizeof(double));
        E[i] = (double*)malloc(n * sizeof(double));
        V[i] = (double*)malloc(n * sizeof(double));
    }

    printf("Enter the elements of the %dx%d matrix row-wise:\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &A[i][j]);
        }
    }

    for (int i = 0; i < 1200; i++) {
        double* temp = (double*)malloc(n * sizeof(double));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                E[i][j] = 0;
                V[i][j] = 0;
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                temp[i] = A[i][k];
            }

            double Two_norm = 0;
            for (int j = 0; j < k; j++) {
                double projection = 0;
                for (int i = 0; i < n; i++) {
                    projection += A[i][k] * E[i][j];
                }
                for (int i = 0; i < n; i++) {
                    temp[i] -= projection * E[i][j];
                }
            }

            for (int i = 0; i < n; i++) {
                Two_norm += pow(temp[i], 2);
            }
            Two_norm = sqrt(Two_norm);

            for (int i = 0; i < n; i++) {
                E[i][k] = temp[i] / Two_norm;
            }

            for (int j = k; j < n; j++) {
                double projection = 0.0;
                for (int i = 0; i < n; i++) {
                    projection += A[i][j] * E[i][k];
                }
                V[k][j] = projection;
            }
        }

        free(temp);

        double** A_new = (double**)malloc(n * sizeof(double*));
        for (int i = 0; i < n; i++) {
            A_new[i] = (double*)malloc(n * sizeof(double));
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A_new[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    A_new[i][j] += V[i][k] * E[k][j];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = A_new[i][j];
            }
        }

        for (int i = 0; i < n; i++) {
            free(A_new[i]);
        }
        free(A_new);
    }

    printf("Eigenvalues are:\n");
    for (int i = 0; i < n; i++) {
        printf("%.7lf ", A[i][i]);
    }
    printf("\n");

    for (int i = 0; i < n; i++) {
        free(A[i]);
        free(E[i]);
        free(V[i]);
    }
    free(A);
    free(E);
    free(V);

    return 0;
}

